# BARA DUEL — Game Design v0.1

> การ์ดเกมดวล 18+ สาย Bara · ผู้เล่นทุกตัวเป็นผู้ใหญ่ · เน้น "คอมโบสนุก" ด้วยการ์ดน้อย และใช้ภาพน้อย

---

## 1. หลักคิด 3 ข้อ

1. **ภาพน้อย แต่ดูขยับเยอะ** — 1 ตัวละคร = ภาพวาด 1 ชุด แยกเลเยอร์ แล้วให้โค้ดทำเอฟเฟกต์ (เด้ง, คัตอิน, เสื้อแตก) แทนการวาดภาพใหม่
2. **การ์ดน้อย คอมโบเยอะ** — การ์ดทั้งเกมราว 26 ใบ คอมโบเกิดจาก "การต่อสัญลักษณ์" ไม่ใช่จากจำนวนการ์ด
3. **เสื้อแตก = ดาบสองคม** — ถอดเสื้อศัตรูได้ แต่ตัวที่ถอดแล้วจะ "แรงขึ้น" ต้องคิดว่าจะถอดแล้วจบให้ได้ในเทิร์นเดียวไหม

---

## 2. กลไกหลัก: **Pose Chain (ต่อท่า)**

การ์ดทุกใบมีสัญลักษณ์ 2 ตัว: **ขาเข้า → ขาออก**

| ไอคอน | ชื่อ | อารมณ์ |
|---|---|---|
| 💪 | Flex | พลัง / โจมตี |
| 🔥 | Heat | ร้อนแรง / ฉีก |
| 💦 | Sweat | อึด / ฟื้นตัว |
| ❤️ | Charm | เสน่ห์ / ควบคุม |
| ⭐ | Wild | ต่อกับอะไรก็ได้ |

ในเทิร์นของเรา ถ้าการ์ดใบถัดไปมี **ขาเข้า ตรงกับ ขาออก** ของใบก่อน → **Chain +1** (เหมือนโดมิโน)

| Chain | รางวัล |
|---|---|
| 2+ | การ์ดที่ต่อ Chain **ลดค่าร่าย 1** (ต่ำสุด 0) |
| 3 | **PUMP!** — Hunk ของเราทุกตัว Power +1 เทิร์นนี้ · คัตอินเล็ก |
| 4+ | **BURST!** — คัตอินเต็มจอ · เลือก Hunk 1 ตัวโจมตีพิเศษ 1 ครั้งที่ **ฉีกเสื้อเป้าหมายหมดทุกชั้น** |

ต่อไม่ตรง = Chain รีเซ็ตเป็น 1 (ยังเล่นได้ แค่เสียโบนัส)

> ทำไมสนุกด้วยการ์ดน้อย: การ์ด 26 ใบ × ลำดับการเล่น = เส้นทางคอมโบเป็นร้อยแบบ ผู้เล่นจะ "อ่านมือ" แบบต่อจิ๊กซอว์ทุกเทิร์น

---

## 3. สนาม & เทิร์น

```
   [ฝั่งศัตรู]   เลน1   เลน2   เลน3
                 ----   ----   ----
                 [ SCENE (ฉากกลาง ใช้ร่วมกัน) ]
                 ----   ----   ----
   [ฝั่งเรา]     เลน1   เลน2   เลน3
```

- Stamina เริ่ม **20** — ลดเหลือ 0 แพ้
- มือเริ่ม 5 ใบ · จั่ว 2/เทิร์น · มือสูงสุด 7
- **AP 3 ต่อเทิร์น** (คงที่ ไม่ต้องสะสม · คนเล่นก่อนเทิร์นแรกได้ 2)
- เด็ค 20 ใบ ซ้ำได้ใบละ 2

**ลำดับเทิร์น**
1. **Draw** จั่ว 2
2. **Main** ลง Hunk / ใช้ Move / ลง Scene / ใช้สกิล — ต่อ Chain ไปเรื่อยๆ
3. **Clash** Hunk ของเราทุกตัว (ที่ไม่ได้เพิ่งลง) ตีเลนตรงข้ามอัตโนมัติ
   - เลนตรงข้ามว่าง → ตี Stamina ศัตรูเท่ากับ Power
4. **End** เคลียร์บัฟเทิร์นนี้

---

## 4. ระบบเสื้อผ้า (Outfit) — หัวใจของเกม

Hunk แต่ละตัวมี **Power / Grit (เลือด) / Outfit (ชั้นเสื้อ 0–2)**

- โดนตี 1 ครั้ง ขณะยังมีเสื้อ → **เสื้อแตก 1 ชั้น** ดาเมจถูกดูดหมด ไม่ว่าแรงแค่ไหน
- ไม่มีเสื้อแล้ว → ดาเมจเข้า Grit · Grit 0 = น็อก
- เสื้อเหลือ 0 → เข้าโหมด **BARE** : **Power +2** และสกิล Bare ทำงาน

ผลต่อเกม:
- ตัวตีแรงทีเดียว (สายล่ำ) เสียเปรียบกับตัวเสื้อหนา
- ตัวตีหลายที (สายนาก) เป็นตัวแกะเสื้อ
- จะถอดเสื้อศัตรู ต้องเตรียมฆ่าให้จบ ไม่งั้นมันแรงขึ้นตีกลับ
- บางทีเรา **ถอดเสื้อตัวเอง** เพื่อเปิด Bare ให้แรงเอง (คอมโบหลัก)

**คีย์เวิร์ด** (มีแค่ 3 คำ)
- **Rush** — ตีได้ในเทิร์นที่ลง
- **Thick** — ดาเมจเข้า Grit ครั้งแรกของแต่ละเทิร์น −1
- **Double** — ตี 2 ครั้ง (= แกะเสื้อ 2 ชั้น)

---

## 5. สาย (Tribe) — 4 สาย

| สาย | บทบาท | จุดเด่น |
|---|---|---|
| 🐻 หมี (Bear) | แทงก์ | Grit สูง เสื้อหนา Thick |
| 💪 ล่ำ (Jock) | บุกหนัก | Power สูง Rush เสื้อบาง |
| 🧔 ป๋า (Daddy) | ซัพพอร์ต | บัฟเพื่อน สั่งถอดเสื้อ |
| 🦦 นาก (Otter) | เทคนิค | ถูก ตีสองที ไอคอน Wild |

โบนัสสาย: Hunk ที่อยู่เลนติดกันและเป็นสายเดียวกัน → Power +1 ทั้งคู่ (คัตอินคู่ได้ด้วย)

---

## 6. รายการการ์ด (26 ใบ)

### Hunk (12 ใบ — ต้องใช้ภาพ)
รูปแบบ: `ค่าร่าย | P/G/O | ขาเข้า→ขาออก | สกิล`

**🐻 หมี**
1. **บิ๊กเบน** `2 | 2/5/2 | 💦→🔥` Thick · *Bare:* ศัตรูเลนตรงข้าม Power −1
2. **ลุงต้น** `1 | 1/3/1 | 🔥→💦` ลงสนาม: เพื่อนเลนติดกัน Outfit +1 ("ใส่เสื้อให้")
3. **จอมพล** `3 | 3/7/2 | 💦→💦` Thick · *Bare:* หมีของเราทุกตัว Power +1

**💪 ล่ำ**
4. **ไทเกอร์** `2 | 4/3/1 | 💪→🔥` Rush
5. **นนท์ ยิมบอย** `1 | 2/2/1 | 🔥→💪` ถ้าลงแบบต่อ Chain: Power +2 เทิร์นนี้
6. **แชมป์ ร็อค** `3 | 5/4/1 | 💪→💪` *Bare:* ตีน็อกแล้วดาเมจเหลือทะลุเข้า Stamina

**🧔 ป๋า**
7. **ป๋าเดฟ** `2 | 2/4/2 | ❤️→💪` เพื่อนเลนติดกัน Power +1
8. **เฮียหมิง** `1 | 1/3/1 | ❤️→❤️` ลงสนาม: จั่ว 1
9. **ผู้กองแดน** `3 | 3/5/2 | 💪→❤️` เทิร์นละครั้ง: สั่ง Hunk ของเรา 1 ตัว **ถอดเสื้อ 1 ชั้น** ("ถอด!")

**🦦 นาก**
10. **ฟ้า** `1 | 1/2/0 | ⭐→💦` Double · เริ่มมาแบบ Bare เลย
11. **เจ** `2 | 2/3/1 | 💦→⭐` Double
12. **คิว** `2 | 1/3/1 | ⭐→⭐` ลงสนาม: นับ Chain +2 แทน +1

### Move (10 ใบ — ไม่ต้องใช้ภาพใหม่)
13. **ดึงเสื้อ** `1 | 🔥→💪` Hunk ใดก็ได้ เสื้อแตก 1 ชั้น (ของเราก็ได้)
14. **ปั๊มกล้าม** `1 | 💪→💦` Hunk 1 ตัว Power +2 เทิร์นนี้
15. **ราดน้ำ** `1 | 💦→❤️` เป้าหมายโดนตีครั้งถัดไป เสื้อแตก 2 ชั้น ("เสื้อเปียก")
16. **ขยิบตา** `1 | ❤️→🔥` Hunk ศัตรู 1 ตัว ไม่ตีใน Clash ถัดไป
17. **แตะมือ** `1 | ❤️→❤️` คืน Hunk เราขึ้นมือ (เสื้อกลับมาเต็ม ลงใหม่ใช้สกิลซ้ำได้)
18. **ล็อกคอ** `2 | 💪→🔥` Hunk เราตีเลนตรงข้ามทันที 1 ครั้ง
19. **เหงื่อท่วม** `1 | 🔥→💦` จั่ว 2
20. **ผ้าเช็ดตัว** `1 | 💦→⭐` Outfit +1 และฟื้น Grit 2
21. **โพสต์ท่า** `0 | ⭐→⭐` ไม่มีผล แค่ต่อ Chain (เทิร์นละ 1 ใบ)
22. **ไฟนอล ฟิสต์** `3 | ⭐→—` ใช้ได้เมื่อ Chain ≥3 · ดาเมจ 5 ข้ามเสื้อทุกชั้น + คัตอินเต็มจอ (จบ Chain)

### Scene (4 ใบ — ใช้แค่ภาพพื้นหลัง)
23. **ยิม** — การ์ดขาออก 💪 ลดค่าร่าย 1
24. **ซาวน่า** — จบเทิร์น Hunk ทุกตัวที่มีเสื้อ แตก 1 ชั้น (ไอน้ำ — ทุกคนเข้า Bare เร็ว เกมจะดุ)
25. **ห้องล็อกเกอร์** — Hunk ใครเข้า Bare เจ้าของจั่ว 1
26. **ชายหาด** — Outfit สูงสุดของทุกตัว = 1

---

## 7. ตัวอย่างคอมโบ

**A. "ถอดเองแรงกว่า"** (ใช้ AP แค่ 1)
บนสนามมี ผู้กองแดน + จอมพล (เสื้อ 2)
1. ขยิบตา `❤️→🔥` (1 AP) — สตันศัตรูตรงหน้าจอมพล
2. ดึงเสื้อ `🔥→💪` (Chain 2 → 0 AP) — ถอดเสื้อจอมพลเอง เหลือ 1
3. ผู้กองแดนสั่ง "ถอด!" → จอมพล **BARE** (+2, หมีทั้งทีม +1)
4. ปั๊มกล้าม `💪→💦` (Chain 3 → 0 AP) → **PUMP!**
→ จอมพล Power 3+2+1+2+1 = **9** และยังเหลือ 2 AP

**B. "เสื้อเปียก"** — แกะหมีเสื้อหนา
ราดน้ำ ใส่หมีศัตรู → ลง เจ (`💦→⭐`, Double) ตีครั้งแรกเสื้อแตก 2 ชั้นหมด ครั้งที่สองเข้าเนื้อ

**C. "BURST เร็ว"**
โพสต์ท่า `⭐→⭐` (0 AP, Chain 1) → คิว `⭐→⭐` (Chain +2 = 3 → **PUMP**, 1 AP) → เจ `💦→⭐` (Chain 4 → **BURST**, 1 AP) ฉีกเสื้อเป้าหมายหมด → เทิร์นถัดไปปิดด้วย ไฟนอล ฟิสต์

---

## 8. ภาพ & เอฟเฟกต์ — ทำยังไงให้เจนภาพน้อย

### งานภาพทั้งหมด
| อย่าง | จำนวน | หมายเหตุ |
|---|---|---|
| ภาพ Hunk | **12 ภาพ** | 1 ภาพ/ตัว แยกเลเยอร์ |
| พื้นหลัง Scene | 4 ภาพ | ใช้เป็นพื้นสนามด้วย |
| การ์ด Move | 0 | ใช้ตัวอักษรเสียงมังงะ (SFX) + ไอคอน หรือครอปจากภาพ Hunk |
| กรอบการ์ด | 1 ชุด | 4 สีตามสาย |

### เลเยอร์ต่อ 1 ตัวละคร (จากภาพเดียว)
```
[หน้า ปกติ / เจ็บ / ยิ้มเยาะ]   ← สลับแค่หัว 3 แบบ
[เสื้อผ้า]                      ← เลเยอร์ที่จะ "แตก"
[ร่าง]                          ← วาดเต็มไว้ใต้เสื้อ
[พื้นหลัง/เงา]
```

### เอฟเฟกต์ (ทำด้วยโค้ด ไม่ต้องวาดเพิ่ม)
- **โอเวอร์เฟรม** — ภาพร่างถูก mask ด้วยกรอบการ์ด แต่หัว/แขนอยู่อีกเลเยอร์ที่ไม่ mask → ทะลุกรอบออกมา ตอนลงการ์ด ซูมเข้า + กระแทก
- **เด้งดึ๋ง** — ใส่ "กระดูกฟิสิกส์" ที่อก/พุง/ก้น (Spine 4.2 Physics หรือ Live2D) + หายใจ idle + squash-stretch ตอนลง/ตอนโดนตี
- **คัตอิน** — ครอปภาพเดิมเป็นแถบเฉียง (ตา / อก) + speedline + ตัวหนังสือ SFX ใช้ตอน PUMP / BURST / ไฟนอล
- **เสื้อแตก** — หั่นเลเยอร์เสื้อเป็นเศษแบบ Voronoi ด้วยโค้ด → ปลิวออก + เศษผ้า particle + จอสั่น + สลับหน้าเป็น "เจ็บ"
  - ชั้นที่ 1 แตก: ลบเสื้อบางส่วน (mask ขาด)
  - ชั้นสุดท้ายแตก: เลเยอร์เสื้อหายหมด → BARE + ออร่า + คัตอิน

---

## 9. เทคนิค & แพลตฟอร์ม (ข้อเสนอ)

- **ต้นแบบเร็ว:** เว็บ (PixiJS + Spine runtime) เล่นในเบราว์เซอร์ได้เลย
- **ตัวจริง:** Godot 4 (ฟรี, export PC/Steam ได้)
- **ช่องทางขาย 18+:** Steam (ติดแท็ก adult), itch.io — **App Store / Play Store ไม่รับเนื้อหาเปลือย**
- ต้องมี age gate และระบุชัดว่าตัวละครทุกตัวเป็นผู้ใหญ่

---

## 10. ขั้นต่อไป

1. **ทดสอบบนกระดาษก่อน** — ปริ้นท์การ์ด 26 ใบ (ยังไม่ต้องมีภาพ) เล่นจริงสัก 5–10 เกม ปรับตัวเลข
2. ทำภาพตัวละครตัวแรก 1 ตัว แยกเลเยอร์ → ทดลองเอฟเฟกต์ (เด้ง / คัตอิน / เสื้อแตก)
3. ทำต้นแบบดิจิทัล: สนาม 3 เลน + Chain + Clash + AI ง่ายๆ

---

## 11. Art direction (PixelLab) — v0.2

- Style: 16-bit fighting-game pixel art, **realistic heroic proportions** (≈8 heads tall, small head, long thick legs), bold dark outline, warm skin shading. Never chibi.
- Method: Pro Flash `create-image-pro-flash` at **128×180** (portrait, fits card) with the user's barbarian sprite as `style_image`, then `edit-image-pixen` for each strip stage (same pose).
- Each card = 1 base image + 1 edit per outfit layer. Cloth-only shards are diffed locally (no extra generations).
- Every character's pose, outfit and weapon/prop must sell their skill. Weapons mix modern and retro. Inner layers and underwear never repeat.
- Continuity rule: every edit prompt repeats the exact wording of the layers that must stay (e.g. "keep exactly the same see-through black mesh tank top"), and every stage is checked side by side before it goes in the game.
- Concealed-nude stages: the concealing hand/weapon/prop must already be in front of the hips in the clothed base pose, so the strip keeps the fighting pose.
- Heat limits: pubic hair, low-rise waistbands, bulges, sheer/wet fabric and bare buttocks are in; genitals are never shown.
- Weapons and props stay in hand through every strip stage. Accessories like a harness can stay on in the bare stage.

| Card | Skill | Pose | Weapon / prop | Outer → inner | Bare stage | Art |
|---|---|---|---|---|---|---|
| บิ๊กเบน (bear) | Thick tank | arms crossed, planted stance | (axe, if redone) | red flannel → olive tank + jeans | navy briefs | done |
| จอมพล (bear) | BARE buffs all bears | salute | cavalry saber, boot on a battle tank | officer greatcoat + medals → black mesh tank + cargo | black jockstrap | done |
| ป๋าเดฟ (daddy) | buffs neighbours | pointing, hand on gun | revolver, sheriff badge, cowboy hat | leather vest + western shirt → leather chest harness + jeans | harness + leather briefs | done |
| แชมป์ ร็อค (jock) | overflow damage | boxing guard | gloves, championship belt | gold satin robe | low-cut red wrestling singlet | done |
| ลุงต้น (bear) | dresses allies | offering a folded shirt | glowing magic sewing needle | knit cardigan over sheer wet see-through undershirt + trousers | low-slung white boxers, pubic trail | done |
| ไทเกอร์ (jock) | Rush | low lunge, front knee raised | twin combat knives | hooded fight vest + MMA shorts | black sport boxer briefs | done |
| นนท์ ยิมบอย (jock) | +2 when chained | double-biceps flex | kettlebell | gym hoodie + joggers | low-rise posing trunks, pubic trail | done |
| เฮียหมิง (daddy) | draw 1 | rear 3/4 view, looking over shoulder | glowing magic cards | red silk shirt slipping off + slacks | red silk thong, bare butt | done |
| ผู้กองแดน (daddy) | orders "ถอด!" | pointing an order, rifle held low across hips | assault rifle | army jacket + cap → stringer tank + fatigues | olive jockstrap + cap | done |
| ฟ้า (otter) | Double, starts bare | dagger raised, hand on towel knot | dagger | (towel card adds open hoodie) | towel slipped low, held over crotch | done |
| เจ (otter) | Double | back view drawing a bow | recurve bow + quiver strap | ranger hooded tunic + leggings | jockstrap, bare butt | done |
| คิว (otter) | chain +2 | spellbook raised, staff across hips | jeweled staff + spellbook | sequin jacket + pants | nude + body chain, staff jewel conceals | done |
