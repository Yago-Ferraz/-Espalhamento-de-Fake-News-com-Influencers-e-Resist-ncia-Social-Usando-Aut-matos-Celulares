from fake_news_sim import FakeNewsSimulation

# Aqui você pode ajustar os parâmetros se quiser
sim = FakeNewsSimulation(
    grid_size=80,
    cell_size=10,
    fps=12,
    prob_share=0.6,
    resistance_rate=0.1,
    threshold=1,
    initial_infected=10,
    delay_max=3,
    influencer_count=400,
    influencer_break_resistance_chance=0.7
)

sim.run()  
