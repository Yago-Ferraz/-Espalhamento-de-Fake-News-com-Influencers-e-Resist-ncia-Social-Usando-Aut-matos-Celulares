# 🧠 Modelagem do Espalhamento de Fake News com Influencers e Resistência Social Usando Autômatos Celulares

Este projeto apresenta uma simulação baseada em autômatos celulares para modelar o espalhamento de fake news em redes sociais. A proposta foi desenvolvida no contexto diciplinar de **Autômatos Celulares**, explorando elementos como:

- Influência social (influencers com maior poder de propagação)
- Resistência à desinformação (usuários céticos ou críticos)
- Tempo de reação individual (delay para decidir compartilhar ou não)

O código é visualizado em tempo real via `pygame`, e permite observar como pequenas variações no número de influencers podem alterar completamente a dinâmica da propagação.

---

## 📜 Artigo científico

O artigo completo, está disponível neste repositório e pode ser acessado [clicando aqui]([./Modelagem%20do%20Espalhamento%20de%20Fake%20News%20com%20Influenciadores%20Usando%20Aut%C3%B4matos%20Celulares%20(2).docx](https://docs.google.com/document/d/1mTl3mV5xawkhunzX1mf7nLfc9xXROGQ9tsemi4RiYoY/edit?usp=sharing)).


## 🔬 Por que este projeto é relevante?

O modelo proposto se baseia nos capítulos 1 e 2 de **Keeling & Rohani (2011)** — *Modeling Infectious Diseases in Humans and Animals*, usando conceitos de propagação epidêmica adaptados ao universo digital.

Além disso, ele dialoga diretamente com conceitos de sociologia de redes, como **conformismo**, **resistência cultural** e **efeito dos formadores de opinião** — tornando-se uma ferramenta exploratória útil tanto para ciências sociais quanto computacionais.

---

## 📦 Requisitos

Instale as dependências com o `pip`:

```bash
pip install -r requirements.txt
```

## ▶️ Como executar
Após instalar os requisitos, execute o simulador com:

```bash
python fake_news_sim.py
```
Durante a simulação:

Pressione Espaço para pausar ou retomar

Feche a janela para encerrar a execução
