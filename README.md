<h1 align="center">
    &#9729;&#65039; CPTEC-Flask-BS
</h1>

<p align="center">
    Aplicação web Flask para obter e mostrar dados de 
    previsão do tempo fornecidos pelo CPTEC/INPE
</p>

<p align="center">
    <img src="/static/demo.gif?raw=true" 
         alt="CPTEC-Flask-BS demo">
</p>

<h2>
    &#128203; Clonando o repositório:
</h2>

Primeiro, verifique a versão do seu Python.  
Esta aplicação foi desenvolvida utilizando **Python 3.11.1**:

    py --version

Agora, instale o virtualenv (caso não esteja disponível):
    
    py -m pip install virtualenv


Clone o repositório e mude para seu diretório:
    
    git clone https://github.com/MachWheel/Crop-My-GIF.git
    cd Crop-My-GIF


Crie um virtualenv para o projeto e ative-o:
    
    py -m venv venv
    .\venv\Scripts\activate


Instale as dependencias do projeto:
    
    py -m pip install -r requirements.txt

Pronto. Agora você pode executar a aplicação digitando:

    py application.py


<h2>
    &#128736;&#65039; Utilizando no seu projeto:
</h2>

Apenas copie para a raiz do seu projeto os diretórios:

    /cptec
    /forecasts
    /static

E registre o blueprint na inicialização da aplicação:

    application.register_blueprint(forecasts.forecasts_blueprint)

A página para as previsões será registrada no endpoint:

    /previsao

Não esqueça de instalar as dependencias necessárias:

    Flask==2.2.2
    pandas==1.5.3
    requests==2.28.2
    xmltodict==0.13.0
    WTForms==3.0.1