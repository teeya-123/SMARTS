from pathlib import Path

from smarts.sstudio import types as t
from smarts.sstudio import gen_scenario


traffic = t.Traffic(
    flows=[
        t.Flow(
            route=t.Route(begin=("west", 0, 10), end=("east", 0, "max"),),
            rate=1,
            actors={t.TrafficActor("car"): 1},
        )
    ]
)

social_agent_missions = {
    "all": (
        [
            t.SocialAgentActor(
                name="open-agent",
                agent_locator="open_agent:open_agent-v0",
                initial_speed=20,
            ),
        ],
        [
            t.Mission(
                t.Route(begin=("west", 1, 10), end=("east", 0, "max")), task=t.CutIn(),
            )
        ],
    ),
}

scenario = t.Scenario(
    traffic={"all": traffic}, social_agent_missions=social_agent_missions,
)

gen_scenario(scenario, output_dir=str(Path(__file__).parent))
