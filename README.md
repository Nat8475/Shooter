# 🎮 Mountain Shooter

Jogo de nave 2D feito em **Python** com **Pygame**. Você enfrenta ondas de inimigos em fases com fundo em paralaxe, sozinho ou com outra pessoa no mesmo teclado, e no fim grava seu nome no ranking.

## Funcionalidades

- **3 modos de jogo:** 1 jogador, 2 jogadores cooperativo e 2 jogadores competitivo
- **Fases com paralaxe:** cada camada do fundo anda numa velocidade diferente
- **Inimigos** que aparecem com o tempo e atiram de volta
- **Ranking (Top 10)** salvo num banco **SQLite**
- Músicas e efeitos sonoros no menu, nas fases e no placar

## Controles

| Ação | Jogador 1 | Jogador 2 |
| --- | --- | --- |
| Mover | Setas ↑ ↓ ← → | W A S D |
| Atirar | Espaço | Alt esquerdo |

No menu, use ↑ ↓ e **Enter**. No placar, digite um nome de 4 letras e aperte **Enter**. **Esc** sai do ranking.

## Como rodar

Pré-requisito: [Python 3](https://www.python.org/downloads/).

```bash
git clone https://github.com/Nat8475/Shooter.git
cd Shooter
pip install -r requirements.txt
python main.py
```

## Estrutura do código

O código é orientado a objetos e usa os padrões **Factory** e **Mediator**:

| Arquivo | Papel |
| --- | --- |
| `main.py` / `Game.py` | Ponto de entrada e laço principal |
| `Menu.py` | Tela inicial e escolha do modo |
| `Level.py` | Lógica de cada fase (spawn de inimigos, tempo, pontuação) |
| `Entity.py` | Classe base de tudo que aparece na tela |
| `Player.py`, `Enemy.py`, `PlayerShot.py`, `EnemyShot.py`, `Background.py` | Entidades do jogo |
| `entityFactory.py` | Cria as entidades (padrão Factory) |
| `EntityMediator.py` | Colisões e dano entre entidades (padrão Mediator) |
| `Score.py` / `DBProxy.py` | Placar e acesso ao banco SQLite |
| `Const.py` | Constantes: cores, velocidades, vida, teclas, tamanho da janela |
| `assets/` | Imagens e sons |

## Tecnologias

Python · Pygame 2.6 · SQLite
