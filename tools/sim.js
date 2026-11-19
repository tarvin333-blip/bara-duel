// AI-vs-AI balance simulator: node sim.js <games>
const { chromium } = require('playwright');
const N = +(process.argv[2] || 200);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 412, height: 880 } });
  await p.addInitScript(() => {
    try { localStorage.setItem('bd_tutOff', '1'); } catch (e) {}
    window.FAST = true; window.AUTO0 = true;
    const stub = { finished: Promise.resolve(), cancel() {}, set onfinish(f) {} };
    Element.prototype.animate = () => stub;
  });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///home/user/bara-duel/web/index.html');
  const res = await p.evaluate(async (N) => {
    $('#start').hidden = true;
    const plays = {}, wins = {}, out = [];
    const orig = playCard;
    playCard = async (side, idx, t) => { const id = G.p[side].hand[idx]?.def.id; (G.played[side] ||= []).push(id); return orig(side, idx, t); };
    for (let g = 0; g < N; g++) {
      newGame(); G.played = [[], []];
      const t0 = Date.now();
      while (!G.over && G.turn < 60 && Date.now() - t0 < 20000) await new Promise(r => setTimeout(r, 5));
      await new Promise(r => setTimeout(r, 5));
      const w = G.p[0].stamina <= 0 ? 1 : G.p[1].stamina <= 0 ? 0 : -1;
      out.push({ w, turns: G.turn, hp: [G.p[0].stamina, G.p[1].stamina] });
      for (const s of [0, 1]) for (const id of new Set(G.played[s])) { plays[id] = (plays[id] || 0) + 1; if (w === s) wins[id] = (wins[id] || 0) + 1; }
      $('#endM').hidden = true;
    }
    return { out, plays, wins };
  }, N);
  const o = res.out, done = o.filter(x => x.w >= 0);
  const first = done.filter(x => x.w === 0).length / done.length;
  const turns = done.map(x => x.turns).sort((a, b) => a - b);
  console.log(JSON.stringify({ games: o.length, finished: done.length, firstPlayerWin: +first.toFixed(3),
    turnsMedian: turns[turns.length >> 1], turnsP10: turns[Math.floor(turns.length * .1)], turnsP90: turns[Math.floor(turns.length * .9)] }));
  const rows = Object.keys(res.plays).map(k => [k, res.plays[k], +((res.wins[k] || 0) / res.plays[k]).toFixed(2)]).sort((a, b) => b[2] - a[2]);
  console.log(rows.map(r => r.join(':')).join('  '));
  console.log('errors', JSON.stringify(errs.slice(0, 3)));
  await b.close();
})();
