import app.config.my_enum as my_enum


def print_entity(world):
    parts = []
    for eid in world.entity_index.active_ids:
        parts.append(f"eid:{eid}\n")
        parts.extend(print_single_entity(eid, world))
    return "".join(parts)


def print_single_entity(entity, world):
    parts = []
    for component_name, component_values in world.l2.components.items():
        component_label = component_name.__name__
        for attr, value in vars(component_values).items():
            if attr == "moods":
                for mood in my_enum.MOOD:
                    parts.append(
                        f"{component_label}:{attr}:{mood}={value[mood][entity]}\n"
                    )
            else:
                parts.append(f"{component_label}:{attr}={value[entity]}\n")
    return parts
