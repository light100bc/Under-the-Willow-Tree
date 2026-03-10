import numpy as np

import app.config.my_enum as my_enum
from app.domain.simulation.l2.components.attr import EmotionData
from app.domain.commands.change_emotion_command import EmotionChangeCommand


class EmotionSystem:
    def __init__(self, world):
        self.world = world

    def on_marriage(self, data):
        pass

    def process(self, actions, cmd_buffer):
        eids = []
        moods = []
        values = []
        methods = []

        for action in actions:
            if isinstance(action.entity, list):
                eids.extend(action.entity)
                moods.extend(action.mood)
                values.extend(action.value)
                methods.extend(action.method)
            else:
                eids.append(action.entity)
                moods.append(action.mood)
                values.append(action.value)
                methods.append(action.method)

        eids = np.array(eids)
        moods = np.array(moods)
        values = np.array(values)
        methods = np.array(methods)

        emotion_data = self.world.l2.components[EmotionData]

        calc_mask = methods == my_enum.MOOD_METHOD.CALCULATE
        final_eids = []
        final_moods = []
        final_values = []

        if np.any(calc_mask):
            calc_eids = eids[calc_mask]
            calc_moods = moods[calc_mask]
            calc_values = values[calc_mask]

            for mood in np.unique(calc_moods):
                m_mask = calc_moods == mood
                m_eids = calc_eids[m_mask]
                m_vals = calc_values[m_mask]

                acc = np.bincount(m_eids, weights=m_vals)
                ids = np.nonzero(acc)[0]
                vals = acc[ids]

                current = emotion_data.moods[mood][ids]
                new_vals = np.clip(current + vals, 0, 100)

                final_eids.extend(ids)
                final_moods.extend([mood] * len(ids))
                final_values.extend(new_vals)

        if final_eids:
            cmd_buffer.add(
                EmotionChangeCommand(
                    np.array(final_eids),
                    np.array(final_moods),
                    np.array(final_values),
                )
            )

        set_mask = methods == my_enum.MOOD_METHOD.SET
        final_eids = []
        final_moods = []
        final_values = []

        if np.any(set_mask):
            set_eids = eids[set_mask]
            set_moods = moods[set_mask]
            set_values = values[set_mask]

            for mood in np.unique(set_moods):
                m_mask = set_moods == mood
                m_eids = set_eids[m_mask]
                m_vals = set_values[m_mask]

                final_eids.extend(m_eids)
                final_moods.extend([mood] * len(m_eids))
                final_values.extend(m_vals)

        if final_eids:
            cmd_buffer.add(
                EmotionChangeCommand(
                    np.array(final_eids),
                    np.array(final_moods),
                    np.array(final_values),
                )
            )

        return []
