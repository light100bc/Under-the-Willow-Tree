from app.domain.simulation.l2.Entity_Index import EntityIndex
from app.domain.simulation.l2.L2_Components import L2Components
from app.engine.event_bus import EventBus
from app.engine.scheduler import Scheduler
from app.engine.time_system import TimeSystem


class World:
    def __init__(self):

        self.l2 = L2Components(capacity=5000)
        self.entity_index = EntityIndex(5000)

        self.systems = {}
        self.time = TimeSystem()
        self.scheduler = Scheduler(self)
        self.running = False

        self.action_queue = []

        #这个world内的message传输管道
        self.event_bus = EventBus()

    
    
    # ===== System =====
    # ??? 哪里新增system，哪里调用 ???
    def add_system(self, name,system):
        self.systems[name]=system

    # 会改变entity或者component的action放dispatch，查询类的不放
    # def dispatch(self, action):
    #     action.apply(self)
    #     # if isinstance(action, list):
    #     #     for a in action:
    #     #         a.apply(self)
    #     # else:
    #     #     action.apply(self)

    # def dispatch_delay(self,action):
    #     if isinstance(action, list):
    #         self.action_queue.extend(action)
    #     else:
    #         self.action_queue.append(action)

    def update(self):
        """
        单帧推进顺序：
        1. 时间推进
        2. L3 决策生成 action
        3. Scheduler 收集 action
        4. Executor 写回 L2
        5. L2 更新物理世界
        """
        
        # 简单示例：自动让前两个结婚
        # ai_system=self.systems[my_enum.SYSTEM.AISystem]
        # if ai_system:
        #     ai_system.update(self)

        # current_actions = self.action_queue
        # self.action_queue = []
        # for action in current_actions:
        #     action.apply(self)

        # 1️⃣ 时间推进
        self.time.advance()

        actions=[]
        # 2️⃣ L3 生成决策
        # actions = self.l3.generate_actions(self)
        # 可用ai_system.update(self)
        # 需要留一个直接触发action的方法，不能全进queue

        # 3️⃣ 加入调度队列
        for action in actions:
            self.scheduler.schedule(action)

        # 4️⃣ 执行所有动作
        self.scheduler.process()

        # 5️⃣ 更新 L2 物理系统
        # 连续动作
        # self.l2.update()