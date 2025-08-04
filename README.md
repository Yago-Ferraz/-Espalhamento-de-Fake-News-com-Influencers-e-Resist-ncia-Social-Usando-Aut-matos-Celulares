
# 🧠 Modelagem do Espalhamento de Fake News com Influencers e Resistência Social Usando Autômatos Celulares

Este projeto apresenta uma simulação baseada em autômatos celulares para modelar o espalhamento de fake news em redes sociais. Desenvolvido no contexto disciplinar de **Autômatos Celulares** , o modelo combina elementos de redes sociais e dinâmica de contágio para observar fenômenos como:

- Influência social (influencers com maior poder de propagação)
- Resistência individual à desinformação (usuários céticos)
- Tempo de reação (delay para decidir compartilhar ou não)

O sistema é visualizado com `pygame` em tempo real, e também permite gerar **gráficos analíticos e interativos** salvos automaticamente na pasta `apendice/`. O objetivo é explorar como diferentes combinações de agentes e parâmetros influenciam a disseminação da desinformação.

---

## 📜 Artigo científico

O artigo completo, em formato acadêmico, está disponível neste repositório e pode ser acessado [clicando aqui](https://github.com/Yago-Ferraz/-Espalhamento-de-Fake-News-com-Influencers-e-Resist-ncia-Social-Usando-Aut-matos-Celulares/blob/7bbe4cddf12b6e868d83dab398314ed93e4a83b7/Modelagem%20do%20Espalhamento%20de%20Fake%20News%20com%20Influenciadores%20Usando%20Aut%C3%B4matos%20Celulares.pdf).

Ele apresenta os fundamentos do modelo, os experimentos realizados e uma análise comparativa entre o impacto dos influenciadores e a resistência social na propagação da fake news.

---

## 🔍 O que foi descoberto?

Durante a simulação, observou-se que:

> 🔹 **Resistência individual tem impacto mais significativo na contenção do contágio** do que o número absoluto de influenciadores.

Mesmo cenários com 400 influencers foram limitados quando 20% da população era resistente à desinformação. Essa descoberta é discutida e evidenciada no artigo e nos gráficos gerados no projeto.

---

## 📂 Apêndice: gráficos e resultados

A pasta `apendice/` contém os **gráficos gerados automaticamente** com os seguintes recursos:

- Comparações entre diferentes cenários de **influencers** (0, 20, 400)
- Variações de **resistência social** (0%, 20%)
- Gráficos estáticos (`.png`) e interativos (`.html`) com *hover* e zoom via Plotly
- Legendas explicativas e títulos autoexplicativos

Você pode abrir os arquivos `.html` com um navegador para uma análise mais rica e interativa dos resultados.

---

## 🔬 Por que este projeto é relevante?

O modelo adapta os capítulos 1 e 2 de **Keeling & Rohani (2011)** — *Modeling Infectious Diseases in Humans and Animals* — aplicando conceitos epidemiológicos ao comportamento em redes sociais.

Além disso, ele se alinha a tópicos de ciências sociais e computação, como:
- **Conformismo e resistência crítica**
- **Formadores de opinião e "super spreaders"**
- **Modelagem de sistemas sociais complexos**

---

## 📦 Requisitos

Instale as dependências com o comando:

```bash
pip install -r requirements.txt
````

---

## ▶️ Como executar

### 🎮 Modo visual (simulação interativa com Pygame)

```bash
python main.py
```

Durante a execução:

* Pressione **Espaço** para pausar ou retomar a simulação.
* Feche a janela para encerrar.

---

### 📈 Modo analítico (gerar gráficos automaticamente)

```bash
python experimentos.py
```

Isso executará simulações com múltiplas combinações de parâmetros e salvará os gráficos em `apendice/`.

---

## 📁 Organização do repositório

```
.
├── fake_news_sim.py         # Lógica principal da simulação como classe reutilizável
├── main.py               # Executa a simulação interativa
├── graficos.py       # Gera gráficos para os diferentes cenários
├── apendice/             # Contém os gráficos estáticos e interativos
├── requirements.txt      # Dependências (pygame, numpy, plotly, etc.)
└── modelagem....pdf           # Artigo científico com descrição e análise do modelo
