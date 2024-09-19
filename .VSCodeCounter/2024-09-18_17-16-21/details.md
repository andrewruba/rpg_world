# Details

Date : 2024-09-18 17:16:21

Directory /Users/andrewruba/Desktop/projects/rpg_world

Total : 82 files,  3543 codes, 386 comments, 1045 blanks, all 4974 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [README.md](/README.md) | Markdown | 465 | 0 | 147 | 612 |
| [environment.yml](/environment.yml) | YAML | 13 | 4 | 1 | 18 |
| [examples/example_character.py](/examples/example_character.py) | Python | 19 | 4 | 6 | 29 |
| [examples/example_character_stats.py](/examples/example_character_stats.py) | Python | 18 | 9 | 9 | 36 |
| [examples/example_game.py](/examples/example_game.py) | Python | 18 | 6 | 7 | 31 |
| [examples/example_spell.py](/examples/example_spell.py) | Python | 25 | 6 | 7 | 38 |
| [pytest.ini](/pytest.ini) | Ini | 3 | 0 | 1 | 4 |
| [requirements.txt](/requirements.txt) | pip requirements | 18 | 3 | 1 | 22 |
| [scripts/build_install.sh](/scripts/build_install.sh) | Shell Script | 22 | 10 | 10 | 42 |
| [scripts/run_tests.sh](/scripts/run_tests.sh) | Shell Script | 19 | 15 | 7 | 41 |
| [scripts/update_requirements.sh](/scripts/update_requirements.sh) | Shell Script | 9 | 15 | 9 | 33 |
| [setup.py](/setup.py) | Python | 40 | 4 | 5 | 49 |
| [src/rpg_world/__init__.py](/src/rpg_world/__init__.py) | Python | 30 | 4 | 4 | 38 |
| [src/rpg_world/__version__.py](/src/rpg_world/__version__.py) | Python | 1 | 0 | 0 | 1 |
| [src/rpg_world/ability/__init__.py](/src/rpg_world/ability/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/ability/ability.py](/src/rpg_world/ability/ability.py) | Python | 64 | 2 | 15 | 81 |
| [src/rpg_world/ability/spell.py](/src/rpg_world/ability/spell.py) | Python | 42 | 6 | 10 | 58 |
| [src/rpg_world/character/__init__.py](/src/rpg_world/character/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/character/character.py](/src/rpg_world/character/character.py) | Python | 52 | 1 | 11 | 64 |
| [src/rpg_world/character/mage.py](/src/rpg_world/character/mage.py) | Python | 68 | 5 | 15 | 88 |
| [src/rpg_world/combat/__init__.py](/src/rpg_world/combat/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [src/rpg_world/combat/action_queue.py](/src/rpg_world/combat/action_queue.py) | Python | 23 | 0 | 5 | 28 |
| [src/rpg_world/combat/battle_manager.py](/src/rpg_world/combat/battle_manager.py) | Python | 43 | 0 | 7 | 50 |
| [src/rpg_world/combat/turn_order.py](/src/rpg_world/combat/turn_order.py) | Python | 26 | 0 | 7 | 33 |
| [src/rpg_world/effect/__init__.py](/src/rpg_world/effect/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/effect/effect.py](/src/rpg_world/effect/effect.py) | Python | 67 | 7 | 21 | 95 |
| [src/rpg_world/effect/spell_effect.py](/src/rpg_world/effect/spell_effect.py) | Python | 45 | 5 | 14 | 64 |
| [src/rpg_world/event/__init__.py](/src/rpg_world/event/__init__.py) | Python | 3 | 3 | 3 | 9 |
| [src/rpg_world/event/event.py](/src/rpg_world/event/event.py) | Python | 63 | 2 | 16 | 81 |
| [src/rpg_world/event/event_manager.py](/src/rpg_world/event/event_manager.py) | Python | 34 | 0 | 8 | 42 |
| [src/rpg_world/event/trigger.py](/src/rpg_world/event/trigger.py) | Python | 90 | 0 | 26 | 116 |
| [src/rpg_world/formula/__init__.py](/src/rpg_world/formula/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/formula/effect_formula.py](/src/rpg_world/formula/effect_formula.py) | Python | 33 | 0 | 8 | 41 |
| [src/rpg_world/formula/formula.py](/src/rpg_world/formula/formula.py) | Python | 34 | 2 | 11 | 47 |
| [src/rpg_world/game/__init__.py](/src/rpg_world/game/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/game/game.py](/src/rpg_world/game/game.py) | Python | 97 | 15 | 24 | 136 |
| [src/rpg_world/game/game_state.py](/src/rpg_world/game/game_state.py) | Python | 32 | 0 | 7 | 39 |
| [src/rpg_world/item/__init__.py](/src/rpg_world/item/__init__.py) | Python | 4 | 3 | 3 | 10 |
| [src/rpg_world/item/consumable.py](/src/rpg_world/item/consumable.py) | Python | 27 | 2 | 8 | 37 |
| [src/rpg_world/item/equipment.py](/src/rpg_world/item/equipment.py) | Python | 49 | 1 | 10 | 60 |
| [src/rpg_world/item/inventory.py](/src/rpg_world/item/inventory.py) | Python | 38 | 0 | 7 | 45 |
| [src/rpg_world/item/item.py](/src/rpg_world/item/item.py) | Python | 36 | 2 | 9 | 47 |
| [src/rpg_world/place/__init__.py](/src/rpg_world/place/__init__.py) | Python | 4 | 3 | 3 | 10 |
| [src/rpg_world/place/location.py](/src/rpg_world/place/location.py) | Python | 32 | 0 | 7 | 39 |
| [src/rpg_world/place/place.py](/src/rpg_world/place/place.py) | Python | 16 | 1 | 4 | 21 |
| [src/rpg_world/place/position.py](/src/rpg_world/place/position.py) | Python | 32 | 0 | 10 | 42 |
| [src/rpg_world/place/world.py](/src/rpg_world/place/world.py) | Python | 44 | 1 | 11 | 56 |
| [src/rpg_world/quest/__init__.py](/src/rpg_world/quest/__init__.py) | Python | 3 | 3 | 3 | 9 |
| [src/rpg_world/quest/quest.py](/src/rpg_world/quest/quest.py) | Python | 66 | 1 | 14 | 81 |
| [src/rpg_world/quest/quest_manager.py](/src/rpg_world/quest/quest_manager.py) | Python | 46 | 0 | 13 | 59 |
| [src/rpg_world/quest/quest_objective.py](/src/rpg_world/quest/quest_objective.py) | Python | 39 | 0 | 9 | 48 |
| [src/rpg_world/save_load/__init__.py](/src/rpg_world/save_load/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/save_load/load_manager.py](/src/rpg_world/save_load/load_manager.py) | Python | 32 | 0 | 5 | 37 |
| [src/rpg_world/save_load/save_manager.py](/src/rpg_world/save_load/save_manager.py) | Python | 30 | 1 | 6 | 37 |
| [src/rpg_world/stats/__init__.py](/src/rpg_world/stats/__init__.py) | Python | 2 | 3 | 3 | 8 |
| [src/rpg_world/stats/character_stats.py](/src/rpg_world/stats/character_stats.py) | Python | 29 | 0 | 6 | 35 |
| [src/rpg_world/stats/stats.py](/src/rpg_world/stats/stats.py) | Python | 68 | 0 | 17 | 85 |
| [src/rpg_world/utils/__init__.py](/src/rpg_world/utils/__init__.py) | Python | 1 | 3 | 3 | 7 |
| [src/rpg_world/utils/logger.py](/src/rpg_world/utils/logger.py) | Python | 44 | 6 | 14 | 64 |
| [tests/character/test_character.py](/tests/character/test_character.py) | Python | 84 | 12 | 18 | 114 |
| [tests/effect/test_effect.py](/tests/effect/test_effect.py) | Python | 38 | 26 | 22 | 86 |
| [tests/effect/test_spell_effect.py](/tests/effect/test_spell_effect.py) | Python | 74 | 13 | 20 | 107 |
| [tests/event/test_event.py](/tests/event/test_event.py) | Python | 77 | 25 | 30 | 132 |
| [tests/event/test_event_manager.py](/tests/event/test_event_manager.py) | Python | 54 | 7 | 20 | 81 |
| [tests/event/test_trigger.py](/tests/event/test_trigger.py) | Python | 63 | 6 | 15 | 84 |
| [tests/game/test_game.py](/tests/game/test_game.py) | Python | 87 | 0 | 27 | 114 |
| [tests/game/test_game_state.py](/tests/game/test_game_state.py) | Python | 101 | 0 | 21 | 122 |
| [tests/item/test_consumable.py](/tests/item/test_consumable.py) | Python | 31 | 7 | 11 | 49 |
| [tests/item/test_equipment.py](/tests/item/test_equipment.py) | Python | 66 | 19 | 28 | 113 |
| [tests/item/test_inventory.py](/tests/item/test_inventory.py) | Python | 47 | 10 | 16 | 73 |
| [tests/item/test_item.py](/tests/item/test_item.py) | Python | 50 | 17 | 23 | 90 |
| [tests/place/test_location.py](/tests/place/test_location.py) | Python | 28 | 6 | 15 | 49 |
| [tests/place/test_place.py](/tests/place/test_place.py) | Python | 18 | 1 | 5 | 24 |
| [tests/place/test_position.py](/tests/place/test_position.py) | Python | 25 | 6 | 13 | 44 |
| [tests/place/test_world.py](/tests/place/test_world.py) | Python | 54 | 11 | 30 | 95 |
| [tests/quest/test_quest.py](/tests/quest/test_quest.py) | Python | 91 | 5 | 23 | 119 |
| [tests/quest/test_quest_manager.py](/tests/quest/test_quest_manager.py) | Python | 105 | 14 | 29 | 148 |
| [tests/quest/test_quest_objective.py](/tests/quest/test_quest_objective.py) | Python | 60 | 0 | 9 | 69 |
| [tests/save_load/test_load_manager.py](/tests/save_load/test_load_manager.py) | Python | 64 | 13 | 17 | 94 |
| [tests/save_load/test_save_manager.py](/tests/save_load/test_save_manager.py) | Python | 53 | 7 | 15 | 75 |
| [tests/stats/test_character_stats.py](/tests/stats/test_character_stats.py) | Python | 59 | 0 | 15 | 74 |
| [tests/utils/test_logger.py](/tests/utils/test_logger.py) | Python | 44 | 5 | 17 | 66 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)