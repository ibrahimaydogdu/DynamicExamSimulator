"""Metinle eşleşen orijinal şekli olmayan sorular için şematik şekiller (matplotlib).

Her fonksiyon (vals, yol) alır; sekil={"cizim": fonksiyon, "dosya": ...} ile bağlanır.
"""
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

plt.rcParams["font.family"] = ["Times New Roman", "DejaVu Serif"]
plt.rcParams["mathtext.fontset"] = "stix"
MAVI = "#2a7fb8"
GRI = "#8a8a8a"


def _ok(ax, p, q, **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=12, lw=1.4, color=kw.get("c", "k")))


def _olcu(ax, p, q, metin, dx=0, dy=0.0, ha="center"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="<->", mutation_scale=9, lw=0.9, color="k"))
    ax.text((p[0] + q[0]) / 2 + dx, (p[1] + q[1]) / 2 + dy, metin, ha=ha, va="center", fontsize=13,
            bbox=dict(fc="white", ec="none", pad=1))


def s15(vals, yol):
    """Rampadan 30° ile fırlayan motosiklet (h yüksekliğinde rampa)."""
    h = vals["h"]
    fig, ax = plt.subplots(figsize=(5.2, 3.3), dpi=100)
    ax.set_xlim(-1.5, 10)
    ax.set_ylim(-0.9, 4.6)
    ax.axis("off")
    ax.set_aspect("equal")
    # zemin ve rampa (h yüksekliği çizimde 3 birim, değere göre ölçeklenir)
    hy = 0.75 * h
    ax.plot([-1.5, 10], [0, 0], "k", lw=1.5)
    for x in [i * 0.3 for i in range(-5, 34)]:
        ax.plot([x, x - 0.2], [0, -0.2], "k", lw=0.6)
    ax.add_patch(Polygon([[-1.5, 0], [-1.5, hy], [0, hy], [1.6, 0]], fc="#d9d3c3", ec="k", lw=1.2))
    # yörünge (30° yukarı fırlatma)
    a = math.radians(30)
    v, g = 5.0, 5.0
    xs = [i * 0.05 for i in range(0, 200)]
    ys = [hy + math.tan(a) * x - g * x * x / (2 * v * v * math.cos(a) ** 2) for x in xs]
    pts = [(x, y) for x, y in zip(xs, ys) if y >= 0.0]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=MAVI, lw=1.5)
    # A noktası, hız vektörü, açı
    ax.plot([0], [hy], "ko", ms=4)
    ax.text(0.25, hy - 0.45, "A", fontsize=14, style="italic")
    _ok(ax, (0, hy), (1.7 * math.cos(a), hy + 1.7 * math.sin(a)))
    ax.text(1.55 * math.cos(a) + 0.15, hy + 1.55 * math.sin(a) + 0.15, r"$v_A$", fontsize=14)
    ax.plot([0, 2.1], [hy, hy], "k--", lw=0.8)
    ax.text(1.05, hy + 0.12, "30°", fontsize=12)
    # yükseklik ölçüsü
    _olcu(ax, (-0.9, 0), (-0.9, hy), f"{h:g} m", dx=-0.1)
    # motosiklet (basit)
    ax.add_patch(Circle((-0.55, hy + 0.17), 0.17, fc="none", ec="k", lw=1.2))
    ax.add_patch(Circle((0.15, hy + 0.17), 0.17, fc="none", ec="k", lw=1.2))
    ax.plot([-0.55, -0.2, 0.15], [hy + 0.17, hy + 0.5, hy + 0.17], "k", lw=1.2)
    ax.text(5.6, 0.25, "t = 2 s", fontsize=13)
    fig.savefig(yol, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def s25(vals, yol):
    """C ve D motorlarının A ve B bloklarını çektiği düzenek; bloklar arası mesafe d0."""
    d0 = vals["d0"]
    fig, ax = plt.subplots(figsize=(6.4, 2.9), dpi=100)
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1.6, 3.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.plot([-1, 13], [0, 0], "k", lw=1.5)
    for x in [i * 0.3 for i in range(-4, 44)]:
        ax.plot([x, x - 0.2], [0, -0.2], "k", lw=0.6)
    xa = 2.3
    xb = xa + 1.2 + d0 * 1.6
    for x0, ad in ((xa, "A"), (xb, "B")):
        ax.add_patch(Rectangle((x0 - 0.6, 0), 1.2, 1.0, fc="#d9d3c3", ec="k", lw=1.3))
        ax.text(x0, 0.5, ad, fontsize=15, style="italic", ha="center", va="center")
    # motorlar
    for x0, ad in ((-0.3, "C"), (12.4, "D")):
        ax.add_patch(Rectangle((x0 - 0.35, 0), 0.7, 1.4, fc="#c9d6e2", ec="k", lw=1.3))
        ax.text(x0, 1.7, ad, fontsize=15, style="italic", ha="center")
    # kablolar ve hareketli makaralar
    ax.add_patch(Circle((xa - 0.9, 0.5), 0.0, fc="k"))
    ax.plot([-0.3 + 0.35, xa - 0.6], [0.5, 0.5], color="k", lw=1.2)
    ax.plot([12.4 - 0.35, xb + 0.6], [0.5, 0.5], color="k", lw=1.2)
    _ok(ax, (xa + 0.7, 0.5), (xa + 1.6 + 0.1, 0.5))
    _ok(ax, (xb - 0.7, 0.5), (xb - 1.6 - 0.1, 0.5))
    ax.text(xa + 1.0, 1.15, r"$a_A$", fontsize=13)
    ax.text(xb - 1.5, 1.15, r"$a_B$", fontsize=13)
    _olcu(ax, (xa + 0.6, -0.8), (xb - 0.6, -0.8), f"{d0:g} m")
    ax.text(0.9, 2.55, r"$a_C = 3t^2$".replace("3", f"{vals['c']:g}"), fontsize=13)
    ax.text(9.2, 2.55, r"$a_D = 5$".replace("5", f"{vals['aD']:g}") + " m/s²", fontsize=13)
    fig.savefig(yol, bbox_inches="tight", facecolor="white")
    plt.close(fig)
