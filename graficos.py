import os
import plotly.graph_objects as go
from fake_news_sim import FakeNewsSimulation

output_dir = "apendice"
os.makedirs(output_dir, exist_ok=True)

influencer_options = [0, 20, 400]
resistance_options = [0.0, 0.2]

for influencers in influencer_options:
    for resistance in resistance_options:
        print(f"🔄 Simulando: influencers={influencers}, resistência={resistance}")
        
        sim = FakeNewsSimulation(
            influencer_count=influencers,
            resistance_rate=resistance,
            visualizar=False
        )
        sim.run(max_steps=100)
        stats = sim.get_stats()

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=stats["step"], y=stats["shared"],
            mode='lines+markers',
            name='Compartilharam (Azul)',
            line=dict(color='blue')
        ))

        fig.add_trace(go.Scatter(
            x=stats["step"], y=stats["resisted"],
            mode='lines+markers',
            name='Resistiram (Vermelho)',
            line=dict(color='red')
        ))

        fig.add_trace(go.Scatter(
            x=stats["step"], y=stats["unaware"],
            mode='lines+markers',
            name='Não ouviram (Cinza)',
            line=dict(color='gray')
        ))

        fig.update_layout(
            title=f"Propagação de Fake News<br><sub>Influencers: {influencers} | Resistência: {int(resistance*100)}%</sub>",
            xaxis_title="Passos do tempo",
            yaxis_title="Número de pessoas",
            legend_title="Estados",
            template="plotly_white",
            hovermode="x unified"
        )

        # Salva como HTML interativo
        filename = f"grafico_interativo_inf{influencers}_res{int(resistance * 100)}.html"
        filepath = os.path.join(output_dir, filename)
        fig.write_html(filepath)
        print(f"✅ Gráfico interativo salvo: {filepath}")
