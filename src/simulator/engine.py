import heapq
from dataclasses import dataclass, field

"""

Minimal Simulator som simulerer: 
- at behov oppstår for en reservedel
- hvis behovet er kritisk, settes kjøretøyet ut av drift
- etter en gitt lead time, blir reparasjonen ferdig 
- da blir kjøretøyet operativt igjen 
- underveis regner den ut hvor mange timer kjøretøyet har vært nede (downtime)

"""

# --------- Event queue element ----------
@dataclass(order=True)
class Event:
    time: float
    seq: int
    etype: str = field(compare=False)
    data: dict = field(compare=False, default_factory=dict)

# --------- Minimal simulator ----------
class Sim:
    def __init__(self):
        self.t = 0.0
        self._seq = 0
        self.q = []  # heap
        self.handlers = {}

        # state (minimalt)
        self.vehicle_operational = {"BV206_A_1": True}
        self.downtime = 0.0
        self._last_t = 0.0

    def schedule(self, time, etype, **data):
        self._seq += 1
        heapq.heappush(self.q, Event(time, self._seq, etype, data))

    def on(self, etype, fn):
        self.handlers[etype] = fn

    def _advance_time(self, new_t):
        # akkumulér nedetid mellom events
        dt = new_t - self._last_t
        if dt > 0 and not self.vehicle_operational["BV206_A_1"]:
            self.downtime += dt
        self._last_t = new_t
        self.t = new_t

    def run(self, until):
        while self.q:
            ev = heapq.heappop(self.q)
            if ev.time > until:
                break
            self._advance_time(ev.time)
            self.handlers[ev.etype](self, **ev.data)

        self._advance_time(until)

# --------- Handlers ----------
def need_arises(sim: Sim, critical: bool, lead_time: float):
    print(f"[t={sim.t:5.1f}] Behov oppstår | kritisk={critical}")
    if critical:
        sim.vehicle_operational["BV206_A_1"] = False
    sim.schedule(sim.t + lead_time, "repair_done", critical=critical)

def repair_done(sim: Sim, critical: bool):
    print(f"[t={sim.t:5.1f}] Reparasjon ferdig")
    if critical:
        sim.vehicle_operational["BV206_A_1"] = True

# --------- Run example ----------
if __name__ == "__main__":
    sim = Sim()
    sim.on("need", need_arises)
    sim.on("repair_done", repair_done)

    # to kritiske behov
    sim.schedule(2.0, "need", critical=True, lead_time=10.0)   # nede 10 timer
    sim.schedule(30.0, "need", critical=True, lead_time=7.5)  # nede 7.5 timer

    sim.run(until=100.0)

    print("\nDowntime (timer):", sim.downtime)
    
