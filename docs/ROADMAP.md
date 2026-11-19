# Bara Duel — Autonomous Roadmap

Every 30-minute iteration: take the first unchecked item, finish it end to end
(code + art + test + commit + push + republish the artifact), tick it here, and
report in one short Thai message. One item per iteration; split big items.

## Guardrails
- PixelLab: ≤ 50 generations per iteration. Stop generating if balance < 3,500.
- Every strip stage is checked side by side for continuity (weapon/prop/mask/inner layer) before it ships.
- No visible genitals. Underwear, pubic hair, bare butts, concealment by props are fine.
- All characters are adults.
- Run `node tools/sim_story.js 20` after any balance-affecting change; keep battle ≈ 85–95%, elite ≈ 50–60%, boss ≈ 30–45% for an AI-played starter deck.
- Run the smoke tests (quick duel, meta flow) before publishing.
- Keep the API key out of the repo.

## Queue
- [x] 1. Floor 2 "สังเวียนใต้ดิน": map data + floor select after floor 1 boss; boss "นักชกไร้หน้า" art (3 layers, boxing theme) + mechanic (counter-punch); sauna scenes for ไทเกอร์ and แชมป์ ร็อค; floor-2 event.
- [x] 2. Thread upgrades: spend ด้ายแห่งความผูกพัน to level a hunk (+1 grit / +1 pow, max 3) from the deck screen; show level on cards.
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
