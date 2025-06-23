import asyncio
import asyncpg

async def run():
    try:
        conn = await asyncpg.connect(
            user='gabriel',
            password='romeirosato',
            database='faculdade',
            host='localhost',
            port=5432
        )
        print("✅ Conexão bem-sucedida com o PostgreSQL!")
        await conn.close()
    except Exception as e:
        print("❌ Erro na conexão:", e)

asyncio.run(run())
