from fastmcp import FastMCP
import random

# MCP Sunucusunu tanımlıyoruz
mcp = FastMCP("Hava Durumu ve Selam Sunucusu")

# 1. ARAÇ (TOOL): Kullanıcıya rastgele bir hava durumu verir
@mcp.tool()
def hava_durumu_getir(sehir: str) -> str:
    """Belirtilen şehir için anlık hava durumunu tahmin eder."""
    durumlar = ["Güneşli", "Bulutlu", "Hafif Yağmurlu", "Rüzgarlı"]
    derece = random.randint(15, 30)
    return f"{sehir} şehrinde hava şu an {random.choice(durumlar)} ve {derece} derece."

# 2. KAYNAK (RESOURCE): Statik bir bilgi kaynağı ekler
@mcp.resource("bilgi://proje-notu")
def proje_notu() -> str:
    """Projenin amacı hakkında kısa bir not."""
    return "Bu sunucu FastMCP kullanılarak ödev amacıyla üretilmiştir."

if __name__ == "__main__":
    mcp.run()