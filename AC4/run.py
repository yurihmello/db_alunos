from app import app, db
import os

if __name__== "__main__":
    #cria Banco
    db.create_all()
    # executa a aplicação
    port = int(os.environ.get("PORT", 8000))
    app.run()
