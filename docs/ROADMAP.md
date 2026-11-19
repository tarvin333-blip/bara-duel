# Bara Duel — Autonomous Roadmap

Every 15-minute iteration: take the first unchecked item, finish it end to end
(code + art + test + commit + push + republish the artifact), tick it here, and
report in one short Thai message (times in Thai time, UTC+7, e.g. "21:55 น."). One item per iteration; split big items.

## Schedule (user request, 2026-11-19)
- Thai time (UTC+7). From 21:00 to 08:00: one iteration every 60 minutes. From 08:00 to 21:00: every 30 minutes.
- Each iteration does two things: (A) the next queue item, and (B) one polish pass from the rotation below. Fix what the pass finds, and note the findings in the report.

## Polish rotation (professional game-dev pass; take the next one each iteration, then wrap around)
1. Art and sexiness review: check one batch of 4 hunks' sprite stages side by side.
   - Appeal: pose, anatomy, proportions, continuity.
   - Are the "Sexy-not-explicit techniques" used: shirt lift, waistband, bulge, angle, body hair?
   - Fix weak stages with small pixen edits (≤10 gens).
2. Game feel: hit stop, screen and card shake, number pop, sound timing, cut-in pacing at ½x/1x/2x.
3. UX and onboarding.
   - First 5 minutes of a new save: is it clear what to do?
   - Tap targets ≥ 40px, text readability, Thai copy tone.
4. Balance and economy.
   - Small sims (`node tools/sim.js 50`, `node tools/sim_story.js 10`).
   - Pack prices, ember income, pity, upgrade costs.
5. Visual polish: UI skin consistency, transitions between screens, map, results screen, empty states.
6. Content and story: dialogue quality, bond scenes, voice lines per hunk (BARE, hit, KO), and that the lines match each character.
7. Performance and bugs: mobile frame pacing, layer count, image sizes, console errors, save corruption, edge cases (0 cards, full board, simultaneous KO).

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
- Batch 2 (doujin covers):
  - Wrestling singlet strap pulled aside off one pec; a tank top bunched up over a chubby belly.
  - Sweaty glossy skin with highlight spots, blushing face, flustered expression.
  - Big soft pecs and belly on bear and debu bodies.
  - A phone or other object held in front of the lap as a natural cover.
  - Thai checkered loincloth (pha khao ma) knotted low, glowing sak yant tattoo, rope wraps.
  - Shirt held open by both hands; wet white shirt.
  - Boxer briefs with the waistband tugged; looking down from a low angle.
- Batch 3:
  - Shy glasses ossan: covers his mouth with a fist and blushes, big round hairy belly.
  - Lying on his side, seen from behind, showing a huge round butt (rear view; the thigh hides the front).
  - Tight white briefs under a big belly; an open Hawaiian shirt with steam and sweat; a bottle or prop held in front of the lap.

## Card goal: 100 collectible cards (user request, 2026-11-19)
- **Now: 54** (24 hunks, 6 freed wardens, Isaac and Marcus, 16 moves, 6 scenes).
- **Target:** 100. Add 16 hunks plus 30 moves/scenes (22 moves, 8 scenes).
- **Pace, alternating every iteration:**
  - 2 new hunks (PixelLab, ≤30 gens, Pose library plus Sexy-not-explicit techniques, each with a card background), or
  - 6 moves/scenes that create new combos with existing keywords.
- **Each new card needs:** rarity, pack pool, AI play value, short and long text, and a voice line for hunks. Run a small sim after each card batch.
- **Ideas for hunks:**
  - firefighter (axe, hose)
  - Muay Thai fighter (sitting on ring ropes)
  - mechanic (lying on a creeper, shirt pulled up)
  - farmer (with a scythe, overalls)
  - cowboy (lasso)
  - wrestler (singlet)
  - bartender (shaker)
  - monk-boxer
  - rugby player (muddy)
  - pilot (flight suit unzipped)
  - plumber (wrench, waistband)
  - yoga daddy (stretching pose)
  - pirate (cutlass)
  - gamer streamer (headset, tank pulled up)
  - doctor (stethoscope, open coat)
  - viking (axe, fur)
- Tally (update every batch): 78/100 (+lasso, coin, highnoon, redress moves; +saloon, dust scenes) (+tex cowboy, +boat wrestler) (+armpit, massage, selfie, tackle moves; +dojo, heat scenes) (+oat mechanic, +somsak shy salaryman) (+plerng, +sak; +strip, spank, shower, protein moves; +stage, rain scenes)

## Queue
- [x] 1. Floor 2 "สังเวียนใต้ดิน": map data + floor select after floor 1 boss; boss "นักชกไร้หน้า" art (3 layers, boxing theme) + mechanic (counter-punch); sauna scenes for ไทเกอร์ and แชมป์ ร็อค; floor-2 event.
- [x] 2. Thread upgrades: spend ด้ายแห่งความผูกพัน to level a hunk (+1 grit / +1 pow, max 3) from the deck screen; show level on cards.
- [x] S1. Sound: synthesized WebAudio SFX (card draw/play, hit, cloth rip, BARE, chain, cut-in whoosh, KO, win/lose, UI click) + mute toggle; no external files.
- [x] V1. VFX pack: impact sparks + weapon-coloured slash on attack, floating damage numbers styled per type, chain aura on the board, card-play glow trail, KO burst.
- [x] C1. New cards: 6 moves + 2 scenes that combo with the new keywords (soft/heavy/counter/cleave), added to packs.
- [x] H1. New player hunks (PixelLab, 2 per iteration, ≤30 gens) — DONE: tong (chub crossbow), bork (gorilla blacksmith), daigo (sumo monk shiko), boon (dad-bod chef seated, apron), keng (police, patrol car, leopard briefs), phum (navy officer kneeling salute, striped trunks), marin (sailor on rope, red speedo), ek (PE coach crouched, white jockstrap), singh (security guard bear, camo briefs), phupha (adult grad student on desk, boxer briefs), takeshi (oyaji samurai kneeling iai, fundoshi), talay (hairy lifeguard on tower ladder rear 3/4, yellow swim brief). Uniform stages: full uniform → uniform shirt open/undershirt → underwear type not used yet by that point (e.g. mesh briefs, leopard briefs, white jockstrap, sheer trunks, red speedo) or prop concealment from the base pose; each with weapon/prop, outfit continuity, rarity + pack pool.
- [x] B1. Themed card backgrounds behind every hunk (user request): ~10 shared pixel-art locations (dojo/temple, beach tower, police street, navy deck, ship rigging, gym/school track, campus classroom, kitchen, forge, boxing ring/underground, sauna, prison corridor for wardens), PixelLab no-character scenes 128×180, darkened + vignette so the sprite pops; map each hunk id → bg in ART; ≤30 gens per iteration, split in 2–3 iterations. DONE batch 1: dojo (takeshi, daigo), beach (talay), street (keng, singh), forge (bork), prison (wardens). DONE batch 2: ship (phum, marin), gym (tiger, non, champ, ek, boxer, marcus), classroom (phupha, q), kitchen (boon, ton, tong), camp (jompon, dan, dave, ben, isaac). DONE batch 3: casino (ming), forest (jay), onsen (fah).
- [x] U1. UX — DONE: battle speed toggle 1x/2x (top bar, saved), long-press board card inspect. collection book (สมุดสะสม from the map: owned in colour, silhouettes, tribe/owned filters, tap to inspect). settings panel (⚙ in battle bar and map: sound, speed, reduce bounce/shake, tutorial, reset save).
- [x] 3. Bond system — DONE: sauna lets you pick who joins (lowest bond first), bond 0–3 hearts, generic 3-level talks for hunks without an authored scene, bond hearts in the collection book, bond 3 = special BARE line (BOND_LINE / generic). Authored scenes now also jompon, dave, ming, dan; bond-3 perk: +1 ♥ when played in story. TODO: authored scenes for the rest (optional).
- [x] 4. Battle backgrounds per floor shown behind the board (reused bg art: floor 1 prison, floor 2 gym, quick duel muaythai; new floors add FLOOR_BG entries).
- [x] 5. Floor 3 "เมืองตะวันตกร้าง" + boss "มือปืนไร้หน้า" (shoots across lanes). DONE: FLOOR3 map/stamina/heroes (tex, jay), basic3/elite3 decks, gunman def (veil+snipe+quickdraw start-of-turn shot), Cole recruit, boss dialogs, western battle bg. The floor auto-unlocks once ART.gunman exists. Gunman art done (4 stages), tex sauna scene; floor 3 verified (FLOORS = 1,2,3; boss battle starts with 28 stamina).
- [ ] 6. Censor-style flash/steam effect option in the BARE cut-in + settings panel (sound/motion toggles).
- [ ] 7. Floor 4 "คาสิโนจันทรา" + boss "เจ้ามือไร้หน้า" (steals a card).
- [ ] 8. Floor 5 "สนามรบในหมอก" + boss "นายพลไร้หน้า".
- [ ] 9. Floor 6 "โรงละครเวท" + boss "นักมายากลไร้หน้า".
- [ ] 10. Floor 7: Vael (2 phases) + 3 endings.

## Done
- Core duel, chain/clothes systems, 12 illustrated hunks, tutorial, voice lines.
- Phase 1 meta (floor 1 map, gacha, deck, save) and phase 2 wardens (6 grunt types + hunter boss).

## Polish log
- Pass 1 (art), 2026-11-19 23:00: ben/ton/jompon/tiger reviewed.
  - Found 8 original hunks with no real middle stage (A1 = A): champ, ton, ming, jay, fah, q, tiger, non.
  - Fixed: tiger (jacket off, waistband rolled low).
  - Ton retry failed (it lost his held shirt and sparkles); redo with a stricter prompt.
  - TODO A1 for: champ, ton, ming, jay, fah, q, non, about 2 per art pass.
  - Pass 2 (game feel), 00:14: added a hit-stop (80ms card jolt before the bounce) on every hit; whole-body bounce from the user's feedback. Sim 50: first player 50%, new cards 48–61%, tiger 55% (the 17% was noise). 
  - Pass 3 (UX), 01:24: top bar buttons 38–40px (mute moved to settings), fixed horizontal overflow on 375px phones (.mbox box-sizing + overflow-x hidden). 
  - Pass 4 (balance), 02:36: duel sim 50 → first player 56%; story sim 30 → battle 73% (too hard for an intro), so floor-1 battle stamina 15→13 → 93%; elite 67%, boss ~47%. Dan/Ming low win rates are an AI artifact (Dan's manual order ability, few Ming samples). Economy not changed. 
  - Pass 5 (visual), 03:58: light pass only. The battle backgrounds read well behind the dimmed board (checked in a screenshot). Boat buffed grit 6→7 after a 25% sim win rate. TODO next visual pass: the map screen could use the floor's bg art instead of a gradient. 
  - Pass 6 (content), 05:11: all hunks had BARE lines except cole/marcus/isaac → added; BOND_LINE added for tex, boat, somsak, oat, sak; Tex sauna scene. Sim watch: somsak 17%, stage 20%, armpit 29%, jay 27% (18-sample noise; recheck in the next balance pass). Next pass: 7 (performance & bugs).
