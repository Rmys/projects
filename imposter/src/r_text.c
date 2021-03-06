/* imposter (OO.org Impress viewer)
** Copyright (C) 2004-2005 Gurer Ozen <madcat@e-kolay.net>
** This code is free software; you can redistribute it and/or
** modify it under the terms of GNU General Public License.
*/

#include "common.h"
#include "render_ctx.h"

struct layout_s {
	ikstack *s;
	int w, h;
	int lh;
	char *text;
	int text_len;
	PangoLayout *play;
	int flag;
};

typedef struct text_ctx_s {
	int x, y, w, h;
	GList *layouts;
	char *bullet;
	int bullet_sz;
	int bullet_flag;
	char *id;
	int last_sz;
} text_ctx;

static void
textcat (struct layout_s *lout, char *text, int len)
{
	if (!text) return;
	if (len == 0) len = strlen (text);
	lout->text = iks_stack_strcat (lout->s, lout->text, lout->text_len, text, len);
	lout->text_len += len;
}

static void
textcatv (struct layout_s *lout, ...)
{
	va_list ap;
	char *tmp;

	va_start (ap, lout);
	while (1) {
		tmp = va_arg (ap, char*);
		if (tmp == (char *) lout) break;
		textcat (lout, tmp, 0);
	}
	va_end (ap);
}

static int
get_size (render_ctx *ctx, char *size)
{
	float dpi, cm, px, sz;
	float scr_mm, scr_px;

	scr_mm = gdk_screen_get_height_mm (gdk_screen_get_default ());
	scr_px = gdk_screen_get_height (gdk_screen_get_default ());
	dpi = (scr_px / scr_mm) * 25.4;
//printf("%s\n", size);
	cm = atof (size);
	if (strstr (size, "pt")) cm = cm * 2.54 / 102;
	px = cm * ctx->fact_y;
//printf ("dpi %f, fact_y %f, cm %f, scale_px %f\n", dpi, ctx->fact_y, cm, px);

	sz = px * 72 / dpi;
	return sz * PANGO_SCALE;
}

static int
r_get_font_size (render_ctx *ctx, text_ctx *tc, iks *node)
{
	char *size, *min;
	int sz, mn;

	size = r_get_style (ctx, node, "fo:font-size");
	min = r_get_style (ctx, node, "fo:min-height");
	if (size) {
		sz = get_size (ctx, size);
		if (min) {
//			mn = get_size (ctx, min);
			mn = 0;
			if (mn > sz) sz = mn;
		}
		tc->last_sz = sz;
		return sz;
	}
	return 0;
}

static void
text_span (render_ctx *ctx, text_ctx *tc, struct layout_s *lout, iks *node, char *text, int len)
{
	char buf[20];
	char *attr;
	int size;
	char *esc;

	if (text == NULL) return;
	if (len == 0) len = strlen (text);
	textcat (lout, "<span", 5);
	attr = r_get_style (ctx, node, "fo:color");
	if (attr) textcatv (lout, " foreground='", attr, "'", lout);
	attr = r_get_style (ctx, node, "fo:font-weight");
	if (attr && strcmp (attr, "bold") == 0) textcat (lout, " weight='bold'", 0);
	attr = r_get_style (ctx, node, "style:text-underline");
	if (attr && strcmp (attr, "single") == 0) textcat (lout, " underline='single'", 0);
	attr = r_get_style (ctx, node, "fo:font-style");
	if (attr && strcmp (attr, "italic") == 0) textcat (lout, " style='italic'", 0);
	if (tc->bullet_flag && tc->bullet_sz) size = tc->bullet_sz; else size = r_get_font_size (ctx, tc, node);
	if (size) {
		sprintf (buf, "%d", size);
		textcatv (lout, " size='", buf, "'", lout);
	}
	textcat (lout, ">", 1);
	esc = g_markup_escape_text (text, len);
	textcat (lout, esc, 0);
	free (esc);
	textcat (lout, "</span>", 7);
}

static int
is_animated (render_ctx *ctx, text_ctx *tc, iks *node)
{
	if (!ctx->step_mode) return 0;
	if (!tc->id) return 0;
	while (strcmp (iks_name (node), "draw:page") != 0
		&& strcmp (iks_name (node), "style:master-page") != 0)
			node = iks_parent (node);
	node = iks_find (node, "presentation:animations");
	if (!node) return 0;
	if (iks_find_with_attrib (node, "presentation:show-text", "draw:shape-id", tc->id)) return 1;
	return 0;
}

static void
text_p (render_ctx *ctx, text_ctx *tc, iks *node)
{
	ikstack *s;
	struct layout_s *lout;
	char *attr;
	iks *n1, *n2;

	s = iks_stack_new (sizeof (struct layout_s), 2048);
	lout = iks_stack_alloc (s, sizeof (struct layout_s));
	memset (lout, 0, sizeof (struct layout_s));
	lout->s = s;
	lout->text = NULL;
	lout->text_len = 0;
	lout->flag = 1;
	if (is_animated (ctx, tc, node) && ctx->step_cnt >= ctx->step) lout->flag = 0;
	ctx->step_cnt++;
	lout->play = pango_layout_new (ctx->pango_ctx);

	attr = r_get_style (ctx, node, "text:enable-numbering");
	if (attr && strcmp (attr, "true") == 0) {
		if (iks_child (node) && tc->bullet) {
			tc->bullet_flag = 1;
			text_span (ctx, tc, lout, node, tc->bullet, strlen (tc->bullet));
			text_span (ctx, tc, lout, node, " ", 1);
			tc->bullet_flag = 0;
		}
	}
	for (n1 = iks_child (node); n1; n1 = iks_next (n1)) {
		if (iks_type (n1) == IKS_CDATA) {
			text_span (ctx, tc, lout, node, iks_cdata (n1), iks_cdata_size (n1));
		}
		if (iks_type (n1) == IKS_TAG && iks_strcmp (iks_name (n1), "text:span") == 0) {
			for (n2 = iks_child (n1); n2; n2 = iks_next (n2)) {
				if (iks_type (n2) == IKS_CDATA) {
					text_span (ctx, tc, lout, n1, iks_cdata (n2), iks_cdata_size (n2));
				}
				if (iks_type (n2) == IKS_TAG && iks_strcmp (iks_name (n2), "text:s") == 0) {
					int gargar;
					char *hede;
					hede = iks_find_attrib (n2, "text:c");
					if (hede) {
						for (gargar = 0; gargar < atoi (hede); gargar++)
							textcat (lout, " ", 1);
					} else
						textcat (lout, " ", 1);
				}
				if (iks_type (n2) == IKS_TAG && iks_strcmp (iks_name (n2), "text:a") == 0) {
					text_span (ctx, tc, lout, n1, iks_cdata (iks_child (n2)), iks_cdata_size (iks_child (n2)));
				}
				if (iks_type (n2) == IKS_TAG && iks_strcmp (iks_name (n2), "text:tab-stop") == 0) {
					text_span (ctx, tc, lout, n2, "\t", 1);
				}
				if (iks_type (n2) == IKS_TAG && iks_strcmp (iks_name (n2), "text:page-number") == 0) {
					char buf[32];
					sprintf (buf, "%d", ctx->page_no);
					text_span (ctx, tc, lout, n2, buf, 0);
				}
			}
		}
		if (iks_type (n1) == IKS_TAG && iks_strcmp (iks_name (n1), "text:a") == 0) {
			text_span (ctx, tc, lout, node, iks_cdata (iks_child (n1)), iks_cdata_size (iks_child (n1)));
		}
		if (iks_type (n1) == IKS_TAG && iks_strcmp (iks_name (n1), "text:line-break") == 0) {
			textcat (lout, "\n", 1);
		}
		if (iks_type (n1) == IKS_TAG && iks_strcmp (iks_name (n1), "text:page-number") == 0) {
			char buf[32];
			sprintf (buf, "%d", ctx->page_no);
			textcat (lout, buf, 0);
		}
	}

	if (!lout->text) {
lout->h = 0;
attr = r_get_style (ctx, node, "fo:line-height");
if (attr) {
	int ratio = atoi (attr);
	lout->lh = ratio;
} else {
	lout->lh = 100;
}
tc->layouts = g_list_append (tc->layouts, lout);
//		g_object_unref (lout->play);
//		iks_stack_delete (s);
		return;
	}

	attr = r_get_style (ctx, node, "fo:text-align");
	if (attr) {
		if (strcmp (attr, "center") == 0)
			pango_layout_set_alignment (lout->play, PANGO_ALIGN_CENTER);
		else if (strcmp (attr, "end") == 0)
			pango_layout_set_alignment (lout->play, PANGO_ALIGN_RIGHT);
	}
	pango_layout_set_width (lout->play, tc->w * PANGO_SCALE);
	pango_layout_set_markup (lout->play, lout->text, lout->text_len);
	pango_layout_get_pixel_size (lout->play, &lout->w, &lout->h);
	attr = r_get_style (ctx, node, "fo:line-height");
	if (attr) {
		int ratio = atoi (attr);
		lout->lh = ratio;
	} else {
		lout->lh = 100;
	}
	tc->layouts = g_list_append (tc->layouts, lout);
}

static void
find_bullet (render_ctx *ctx, text_ctx *tc, iks *node)
{
	iks *x;
	char *t;
	x = r_get_bullet (ctx, node, "text:list-level-style-bullet");
	x = iks_find (x, "text:list-level-style-bullet");
	t = iks_find_attrib (x, "text:bullet-char");
	if (t) tc->bullet = t; else tc->bullet = "*";
	x = iks_find (x, "style:properties");
	t = iks_find_attrib (x, "fo:font-size");
	if (t) tc->bullet_sz = tc->last_sz * atoi (t) / 100;
	else tc->bullet_sz = 0;
}

void
text_list (render_ctx *ctx, text_ctx *tc, iks *node)
{
	iks *n1, *n2;

	for (n1 = iks_child (node); n1; n1 = iks_next (n1)) {
		if (iks_type (n1) == IKS_TAG) {
			for (n2 = iks_child (n1); n2; n2 = iks_next (n2)) {
				if (iks_type (n2) == IKS_TAG) {
					if (strcmp (iks_name (n2), "text:p") == 0)
						text_p (ctx, tc, n2);
					else if (strcmp (iks_name (n2), "text:ordered-list") == 0)
						text_list (ctx, tc, n2);
					else if (strcmp (iks_name (n2), "text:unordered-list") == 0) {
						find_bullet (ctx, tc, n2);
						text_list (ctx, tc, n2);
						tc->bullet = 0;
					}
				}
			}
		}
	}
}

void
r_text (render_ctx *ctx, iks *node)
{
	GList *item;
	struct layout_s *lout;
	text_ctx tc;
	iks *n;
	int flag;

	memset (&tc, 0, sizeof (text_ctx));
	tc.x = r_get_x (ctx, node, "svg:x");
	tc.y = r_get_y (ctx, node, "svg:y");
	tc.w = r_get_y (ctx, node, "svg:width");
	tc.h = r_get_y (ctx, node, "svg:height");
	tc.layouts = NULL;
	tc.bullet = NULL;
	tc.bullet_flag = 0;
	tc.last_sz = 0;

	tc.id = iks_find_attrib (node, "draw:id");
	ctx->step_cnt = 0;
	for (n = iks_first_tag (node); n; n = iks_next_tag (n)) {
		if (strcmp (iks_name (n), "text:p") == 0) {
			text_p (ctx, &tc, n);
		} else if (strcmp (iks_name (n), "text:ordered-list") == 0) {
			text_list (ctx, &tc, n);
		} else if (strcmp (iks_name (n), "text:unordered-list") == 0) {
			find_bullet (ctx, &tc, n);
			text_list (ctx, &tc, n);
			tc.bullet = 0;
		}
	}

	flag = 0;
	for (item = g_list_first (tc.layouts); item; item = g_list_next (item)) {
		lout = (struct layout_s *)item->data;
		if (flag) {
			tc.y += flag * 1.2 * lout->lh / 100;
		}
		if (lout->flag) gdk_draw_layout (ctx->d, ctx->gc, tc.x, tc.y, lout->play);
		if (flag) {
			if (lout->h) flag = lout->h;
		} else {
			flag = lout->h;
		}
		g_object_unref (lout->play);
		iks_stack_delete (lout->s);
	}
	g_list_free (tc.layouts);
}
