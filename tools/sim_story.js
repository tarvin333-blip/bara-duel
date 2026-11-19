// Story-battle balance sim: AI plays the starter deck against each node type. node tools/sim_story.js <games per type>
const { chromium } = require('playwright');
const N = +(process.argv[2] || 60);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.addInitScript(() => {
    try { localStorage.setItem('bd_tutOff', '1'); localStorage.removeItem('bd_save_v1'); } catch (e) {}
    window.FAST = true; window.AUTO0 = true;
    const stub = { finished: Promise.resolve(), cancel() {}, set onfinish(f) {} };
    Element.prototype.animate = () => stub;
  });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, '../web/index.html'));
  const out = await p.evaluate(async (N) => {
    $('#start').hidden = true; SV = newSave();
    storyBattleEnd = () => {};   // just measure
    const res = {};
    for (const t of ['battle', 'elite', 'boss']) {
      const r = { win: 0, turns: [] };
      for (let g = 0; g < N; g++) {
        startStoryBattle({ id: 'x', t });
        const t0 = Date.now();
        while (!G.over && G.turn < 80 && Date.now() - t0 < 20000) await new Promise(r => setTimeout(r, 5));
        await new Promise(r => setTimeout(r, 5));
        if (G.p[1].stamina <= 0) r.win++;
        r.turns.push(G.turn); G.over = true;
      }
      r.turns.sort((a, b) => a - b);
      res[t] = { winRate: +(r.win / N).toFixed(2), turnsMedian: r.turns[N >> 1], turnsP90: r.turns[Math.floor(N * .9)] };
    }
    return res;
  }, N);
  console.log(JSON.stringify(out), 'errors', JSON.stringify(errs.slice(0, 3)));
  await b.close();
})();
