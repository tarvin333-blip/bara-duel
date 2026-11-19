# Bara Duel — Autonomous Roadmap

Every 15-minute iteration: take the first unchecked item, finish it end to end
(code + art + test + commit + push + republish the artifact), tick it here, and
report in one short Thai message. One item per iteration; split big items.

## Guardrails
- PixelLab: ≤ 30 generations per iteration. Stop generating if balance < 3,500.
- Every strip stage is checked side by side for continuity (weapon/prop/mask/inner layer) before it ships.
- No visible genitals. Underwear, pubic hair, bare butts, concealment by props are fine.
- All characters are adults.
- Token budget: run sims ONLY when card stats/mechanics/enemy decks change, and keep them small (`node tools/sim.js 50`, `node tools/sim_story.js 10`). Skip sims for UI/sound/VFX/art-only work. Look at one combined contact sheet per new character and at most one screenshot per iteration.
- Run the smoke tests (quick duel, meta flow) before publishing.
- Keep the API key out of the repo.

## Pose library (new characters must NOT use the plain standing 3/4 pose)
Card-game splash poses mixed with art-nude photo-book poses. Each new character takes a pose not used by the previous two, and the pose must still read as that fighter's skill. Seated/kneeling/crouched poses also help conceal the final stage naturally (thigh, knee, prop).
- kneeling on one knee, hand on weapon (iai draw / oath)
- deep squat or sumo shiko stance, one leg raised
- seated on a crate/stool/rock, leaning forward, one knee up, weapon resting across thighs
- reclining back on one elbow, one knee raised (fits a short portrait canvas)
- crouched low on one heel, looking back over the shoulder (rear 3/4)
- leaning back against a post/wall, arms behind head, hips forward
- mid-action: leaping strike, spinning kick, drawing a bow from a crouch
- back view with arched spine, looking over shoulder, arms raised stretching
- hanging from a bar/rope with one arm, body twisted
Planned: sumo monk → shiko stance; dad-bod chef → seated on a crate with cleaver; oyaji samurai → kneeling iai draw; hairy lifeguard → crouched on the tower ladder, rear 3/4.

### Sexy-not-explicit techniques (from the user's reference batch, 2026-11-19)
Use these instead of nudity. Never draw genitals, even when a reference does.
- Shirt lifted by the hand or held in the teeth to show abs; a tank top pulled up over the pecs; arms raised showing hairy armpits.
- Open uniform or dress shirt with suspenders, a lanyard ID or a loose tie on a bare hairy chest; a sheer or wet shirt over the chest only.
- A thumb hooking the waistband down to show the pubic-hair trail (low-rise; the fabric still covers); one side of the shorts pulled aside to show a jockstrap or brief.
- Bulge in tight briefs, jockstrap pouch, mesh shorts or satin shorts; tube socks, sneakers, a cap.
- Camera angles: low angle looking up; seated with knees apart and a forearm or thigh hiding the lap; rear view of a bare butt in a thong or jockstrap, looking over the shoulder; on all fours on the sand in a striped swim brief.
- Nipples, chest hair and belly hair are fine. Body range: hairy dad bod, chubby belly with the shirt pulled up, huge pecs, slim adult swimmer.
- Apron-only chef from the front with the back bare; samurai, warrior or loincloth harness costumes.

## Queue
- [x] 1. Floor 2 "สังเวียนใต้ดิน": map data + floor select after floor 1 boss; boss "นักชกไร้หน้า" art (3 layers, boxing theme) + mechanic (counter-punch); sauna scenes for ไทเกอร์ and แชมป์ ร็อค; floor-2 event.
- [x] 2. Thread upgrades: spend ด้ายแห่งความผูกพัน to level a hunk (+1 grit / +1 pow, max 3) from the deck screen; show level on cards.
- [x] S1. Sound: synthesized WebAudio SFX (card draw/play, hit, cloth rip, BARE, chain, cut-in whoosh, KO, win/lose, UI click) + mute toggle; no external files.
- [x] V1. VFX pack: impact sparks + weapon-coloured slash on attack, floating damage numbers styled per type, chain aura on the board, card-play glow trail, KO burst.
- [x] C1. New cards: 6 moves + 2 scenes that combo with the new keywords (soft/heavy/counter/cleave), added to packs.
- [x] H1. New player hunks (PixelLab, 2 per iteration, ≤30 gens) — DONE: tong (chub crossbow), bork (gorilla blacksmith), daigo (sumo monk shiko), boon (dad-bod chef seated, apron), keng (police, patrol car, leopard briefs), phum (navy officer kneeling salute, striped trunks), marin (sailor on rope, red speedo), ek (PE coach crouched, white jockstrap), singh (security guard bear, camo briefs), phupha (adult grad student on desk, boxer briefs), takeshi (oyaji samurai kneeling iai, fundoshi), talay (hairy lifeguard on tower ladder rear 3/4, yellow swim brief). Uniform stages: full uniform → uniform shirt open/undershirt → underwear type not used yet by that point (e.g. mesh briefs, leopard briefs, white jockstrap, sheer trunks, red speedo) or prop concealment from the base pose; each with weapon/prop, outfit continuity, rarity + pack pool.
- [ ] B1. Themed card backgrounds behind every hunk (user request): ~10 shared pixel-art locations (dojo/temple, beach tower, police street, navy deck, ship rigging, gym/school track, campus classroom, kitchen, forge, boxing ring/underground, sauna, prison corridor for wardens), PixelLab no-character scenes 128×180, darkened + vignette so the sprite pops; map each hunk id → bg in ART; ≤30 gens per iteration, split in 2–3 iterations. DONE batch 1: dojo (takeshi, daigo), beach (talay), street (keng, singh), forge (bork), prison (wardens). DONE batch 2: ship (phum, marin), gym (tiger, non, champ, ek, boxer, marcus), classroom (phupha, q), kitchen (boon, ton, tong), camp (jompon, dan, dave, ben, isaac). TODO: ming, jay, fah (casino/forest/onsen).
- [ ] U1. UX: collection/codex screen (owned/unowned silhouettes, filters), battle speed toggle (1x/2x), long-press card inspect, settings panel.
- [ ] 3. Bond system: sauna scenes for every recruited hunk (incl. freed wardens and Isaac); bond level shown in collection; bond 3 unlocks a special voice line.
- [ ] 4. Battle backgrounds per floor (PixelLab, 2 images) shown behind the board.
- [ ] 5. Floor 3 "เมืองตะวันตกร้าง" + boss "มือปืนไร้หน้า" (shoots across lanes).
- [ ] 6. Censor-style flash/steam effect option in the BARE cut-in + settings panel (sound/motion toggles).
- [ ] 7. Floor 4 "คาสิโนจันทรา" + boss "เจ้ามือไร้หน้า" (steals a card).
- [ ] 8. Floor 5 "สนามรบในหมอก" + boss "นายพลไร้หน้า".
- [ ] 9. Floor 6 "โรงละครเวท" + boss "นักมายากลไร้หน้า".
- [ ] 10. Floor 7: Vael (2 phases) + 3 endings.

## Done
- Core duel, chain/clothes systems, 12 illustrated hunks, tutorial, voice lines.
- Phase 1 meta (floor 1 map, gacha, deck, save) and phase 2 wardens (6 grunt types + hunter boss).
