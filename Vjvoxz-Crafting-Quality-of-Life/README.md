# Minecraft Custom Data Pack Recipe Hierarchy **MCJE 1.21.8**

This document contains a structured directory hierarchy and classification of the recipes defined in the data pack, split into the `cinchmissingblocks`, `custom` and `minecraft` namespaces.

## Table of Contents
1. [Overview](#1-overview)
2. [Directory Tree Hierarchy](#2-directory-tree-hierarchy)
3. [Cinchmissingblocks Namespace (`cinchmissingblocks`)](#3-cinchmissingblocks-namespace-cinchmissingblocks)
    * [back_to_blocks_slabs](#back_to_blocks_slabs)
    * [back_to_blocks_stairs](#back_to_blocks_stairs)
4. [Custom Namespace (`custom`)](#4-custom-namespace-custom)
    * [back_to_blocks_slabs](#back_to_blocks_slabs)
    * [back_to_blocks_stairs](#back_to_blocks_stairs)
    * [botanical_replication](#botanical_replication)
    * [craftable](#craftable)
    * [universal_dyeing](#universal_dyeing)
    * [unpackable](#unpackable)
5. [Minecraft Namespace (`minecraft`)](#5-minecraft-namespace-minecraft)
6. [Recipe Distribution Summary](#6-recipe-distribution-summary)

---

## 1. Overview
This data pack provides extensive customization for crafting mechanics:
* **Cinchmissingblocks Namespace:** Modifies and rebalances Cinchmissingblocks recipes for slabs and stairs.
* **Custom Namespace:** Adds new crafting behaviors, plant replications, dye utilities, and uncrafting/unpacking mechanics.
* **Minecraft Namespace:** Modifies and rebalances vanilla recipes (such as stairs, trapdoors, and wood stripping) to provide higher yields or better consistency.

---

## 2. Directory Tree Hierarchy

recipes/

├── cinchmissingblocks/

│   └── recipe/

│       ├── back_to_blocks_slabs/

│       ├── back_to_blocks_stairs/

├── custom/

│   └── recipe/

│       ├── back_to_blocks_slabs/

│       ├── back_to_blocks_stairs/

│       ├── botanical_replication/

│       ├── craftable/

│       ├── universal_dyeing/

│       └── unpackable/

└── minecraft/
    └── recipe/   

---

## 3. Cinchmissingblocks Namespace (`cinchmissingblocks`)

The `cinchmissingblocks` namespace follows the 'back_to_block_slabs', 'back_to_blocks_stairs and 'more_slabs' and 'more stairs' recipes to expand and rebalance the output for the new blocks.

### back_to_blocks_slabs

Allows players to craft full blocks back from their slab variants, preventing material waste.

* `andesite_bricks_from_slabs.json`
* `black_concrete_from_slabs.json`
* `black_terracotta_from_slabs.json`
* `blackstone_tile_from_slabs.json`
* `blue_concrete_from_slabs.json`
* `blue_nether_bricks_from_slabs.json`
* `blue_terracotta_from_slabs.json`
* `brown_concrete_from_slabs.json`
* `brown_terracotta_from_slabs.json`
* `calcite_bricks_from_slabs.json`
* `calcite_from_slabs.json`
* `cracked_andesite_bricks_from_slabs.json`
* `cracked_blackstone_tile_from_slabs.json`
* `cracked_blue_nether_bricks_from_slabs.json`
* `cracked_bricks_from_slabs.json`
* `cracked_calcite_bricks_from_slabs.json`
* `cracked_deepslate_bricks_from_slabs.json`
* `cracked_deepslate_tile_from_slabs.json`
* `cracked_diorite_bricks_from_slabs.json`
* `cracked_dripstone_bricks_from_slabs.json`
* `cracked_end_stone_bricks_from_slabs.json`
* `cracked_granite_bricks_from_slabs.json`
* `cracked_mud_bricks_from_slabs.json`
* `cracked_nether_bricks_from_slabs.json`
* `cracked_polished_blackstone_bricks_from_slabs.json`
* `cracked_prismarine_bricks_from_slabs.json`
* `cracked_quartz_bricks_from_slabs.json`
* `cracked_red_nether_bricks_from_slabs.json`
* `cracked_red_sandstone_bricks_from_slabs.json`
* `cracked_resin_bricks_from_slabs.json`
* `cracked_sandstone_bricks_from_slabs.json`
* `cracked_stone_bricks_from_slabs.json`
* `cracked_stone_tile_from_slabs.json`
* `cracked_tuff_bricks_from_slabs.json`
* `cyan_concrete_from_slabs.json`
* `cyan_terracotta_from_slabs.json`
* `deepslate_from_slabs.json`
* `diorite_bricks_from_slabs.json`
* `dripstone_bricks_from_slabs.json`
* `dripstone_from_slabs.json`
* `end_stone_from_slabs.json`
* `granite_bricks_from_slabs.json`
* `gray_concrete_from_slabs.json`
* `gray_terracotta_from_slabs.json`
* `green_concrete_from_slabs.json`
* `green_terracotta_from_slabs.json`
* `light_blue_concrete_from_slabs.json`
* `light_blue_terracotta_from_slabs.json`
* `light_gray_concrete_from_slabs.json`
* `light_gray_terracotta_from_slabs.json`
* `lime_concrete_from_slabs.json`
* `lime_terracotta_from_slabs.json`
* `magenta_concrete_from_slabs.json`
* `magenta_terracotta_from_slabs.json`
* `mossy_andesite_bricks_from_slabs.json`
* `mossy_bricks_from_slabs.json`
* `mossy_calcite_bricks_from_slabs.json`
* `mossy_cobbled_deepslate_from_slabs.json`
* `mossy_deepslate_bricks_from_slabs.json`
* `mossy_deepslate_tile_from_slabs.json`
* `mossy_diorite_bricks_from_slabs.json`
* `mossy_dripstone_bricks_from_slabs.json`
* `mossy_end_stone_bricks_from_slabs.json`
* `mossy_granite_bricks_from_slabs.json`
* `mossy_mud_bricks_from_slabs.json`
* `mossy_prismarine_bricks_from_slabs.json`
* `mossy_quartz_bricks_from_slabs.json`
* `mossy_red_sandstone_bricks_from_slabs.json`
* `mossy_resin_bricks_from_slabs.json`
* `mossy_sandstone_bricks_from_slabs.json`
* `mossy_stone_tile_from_slabs.json`
* `mossy_tuff_bricks_from_slabs.json`
* `netherrack_from_slabs.json`
* `orange_concrete_from_slabs.json`
* `orange_terracotta_from_slabs.json`
* `packed_mud_from_slabs.json`
* `pink_concrete_from_slabs.json`
* `pink_terracotta_from_slabs.json`
* `polished_calcite_from_slabs.json`
* `polished_dripstone_from_slabs.json`
* `polished_end_stone_from_slabs.json`
* `purple_concrete_from_slabs.json`
* `purple_terracotta_from_slabs.json`
* `quartz_bricks_from_slabs.json`
* `red_concrete_from_slabs.json`
* `red_sandstone_bricks_from_slabs.json`
* `red_terracotta_from_slabs.json`
* `sandstone_bricks_from_slabs.json`
* `smooth_basalt_from_slabs.json`
* `snow_bricks_from_slabs.json`
* `stone_tile_from_slabs.json`
* `terracotta_from_slabs.json`
* `white_concrete_from_slabs.json`
* `white_terracotta_from_slabs.json`
* `yellow_concrete_from_slabs.json`
* `yellow_terracotta_from_slabs.json`

### back_to_blocks_stairs

Allows players to craft full blocks back from their stair variants, preventing material waste.

## 4. Custom Namespace (`custom`)

The `custom` namespace introduces original crafting mechanics and quality-of-life additions.

### back_to_blocks_slabs

Allows players to craft full blocks back from their slab or stair variants, preventing material waste.

* `acacia_planks_from_slabs.json`
* `andesite_from_slabs.json`
* `bamboo_mosaic_from_slabs.json`
* `bamboo_planks_from_slabs.json`
* `birch_planks_from_slabs.json`
* `blackstone_from_slabs.json`
* `bricks_from_slabs.json`
* `cherry_planks_from_slabs.json`
* `cobbled_deepslate_from_slabs.json`
* `cobblestone_from_slabs.json`
* `crimson_planks_from_slabs.json`
* `cut_copper_from_slabs.json`
* `cut_red_sandstone_from_slabs.json`
* `cut_sandstone_from_slabs.json`
* `dark_oak_planks_from_slabs.json`
* `dark_prismarine_from_slabs.json`
* `deepslate_bricks_from_slabs.json`
* `deepslate_tiles_from_slabs.json`
* `diorite_from_slabs.json`
* `end_stone_bricks_from_slabs.json`
* `exposed_cut_copper_from_slabs.json`
* `granite_from_slabs.json`
* `jungle_planks_from_slabs.json`
* `mangrove_planks_from_slabs.json`
* `mossy_cobblestone_from_slabs.json`
* `mossy_stone_bricks_from_slabs.json`
* `mud_bricks_from_slabs.json`
* `nether_bricks_from_slabs.json`
* `oak_planks_from_slabs.json`
* `oxidized_cut_copper_from_slabs.json`
* `pale_oak_planks_from_slabs.json`
* `polished_andesite_from_slabs.json`
* `polished_blackstone_bricks_from_slabs.json`
* `polished_blackstone_from_slabs.json`
* `polished_deepslate_from_slabs.json`
* `polished_diorite_from_slabs.json`
* `polished_granite_from_slabs.json`
* `polished_tuff_from_slabs.json`
* `prismarine_bricks_from_slabs.json`
* `prismarine_from_slabs.json`
* `purpur_block_from_slabs.json`
* `quartz_block_from_slabs.json`
* `red_nether_bricks_from_slabs.json`
* `red_sandstone_from_slabs.json`
* `resin_bricks_from_slabs.json`
* `sandstone_from_slabs.json`
* `smooth_quartz_from_slabs.json`
* `smooth_red_sandstone_from_slabs.json`
* `smooth_sandstone_from_slabs.json`
* `smooth_stone_from_slabs.json`
* `spruce_planks_from_slabs.json`
* `stone_bricks_from_slabs.json`
* `stone_from_slabs.json`
* `tuff_bricks_from_slabs.json`
* `tuff_from_slabs.json`
* `warped_planks_from_slabs.json`
* `waxed_cut_copper_from_slabs.json`
* `waxed_exposed_cut_copper_from_slabs.json`
* `waxed_oxidized_cut_copper_from_slabs.json`
* `waxed_weathered_cut_copper_from_slabs.json`
* `weathered_cut_copper_from_slabs.json`

### back_to_blocks_stairs

Allows players to craft full blocks back from their stair variants, preventing material waste.

* `acacia_planks_from_stairs.json`
* `andesite_from_stairs.json`
* `bamboo_mosaic_from_stairs.json`
* `bamboo_planks_from_stairs.json`
* `birch_planks_from_stairs.json`
* `blackstone_from_stairs.json`
* `bricks_from_stairs.json`
* `cherry_planks_from_stairs.json`
* `cobbled_deepslate_from_stairs.json`
* `cobblestone_from_stairs.json`
* `crimson_planks_from_stairs.json`
* `cut_copper_from_stairs.json`
* `dark_oak_planks_from_stairs.json`
* `dark_prismarine_from_stairs.json`
* `deepslate_bricks_from_stairs.json`
* `deepslate_tiles_from_stairs.json`
* `diorite_from_stairs.json`
* `end_stone_bricks_from_stairs.json`
* `exposed_cut_copper_from_stairs.json`
* `granite_from_stairs.json`
* `jungle_planks_from_stairs.json`
* `mangrove_planks_from_stairs.json`
* `mossy_cobblestone_from_stairs.json`
* `mossy_stone_bricks_from_stairs.json`
* `mud_bricks_from_stairs.json`
* `nether_bricks_from_stairs.json`
* `oak_planks_from_stairs.json`
* `oxidized_cut_copper_from_stairs.json`
* `pale_oak_planks_from_stairs.json`
* `polished_andesite_from_stairs.json`
* `polished_blackstone_bricks_from_stairs.json`
* `polished_blackstone_from_stairs.json`
* `polished_deepslate_from_stairs.json`
* `polished_diorite_from_stairs.json`
* `polished_granite_from_stairs.json`
* `polished_tuff_from_stairs.json`
* `prismarine_bricks_from_stairs.json`
* `prismarine_from_stairs.json`
* `purpur_block_from_stairs.json`
* `quartz_block_from_stairs.json`
* `red_nether_bricks_from_stairs.json`
* `red_sandstone_from_stairs.json`
* `resin_bricks_from_stairs.json`
* `sandstone_from_stairs.json`
* `smooth_quartz_from_stairs.json`
* `smooth_red_sandstone_from_stairs.json`
* `smooth_sandstone_from_stairs.json`
* `spruce_planks_from_stairs.json`
* `stone_bricks_from_stairs.json`
* `stone_from_stairs.json`
* `tuff_bricks_from_stairs.json`
* `tuff_from_stairs.json`
* `warped_planks_from_stairs.json`
* `waxed_cut_copper_from_stairs.json`
* `waxed_exposed_cut_copper_from_stairs.json`
* `waxed_oxidized_cut_copper_from_stairs.json`
* `waxed_weathered_cut_copper_from_stairs.json`
* `weathered_cut_copper_from_stairs.json`

### botanical_replication

Enables the replication or systematic renewal of botanical variants, plants, and flowers.

* `allium.json`
* `azure_bluet.json`
* `bush.json`
* `cactus_flower.json`
* `closed_eyeblossom.json`
* `cornflower.json`
* `dandelion.json`
* `firefly_bush.json`
* `large_fern.json`
* `lily_of_the_valley.json`
* `lily_pad.json`
* `open_eyeblossom.json`
* `orange_tulip.json`
* `oxeye_daisy.json`
* `pink_tulip.json`
* `pitcher_plant.json`
* `poppy.json`
* `red_tulip.json`
* `spore_blossom.json`
* `tall_dry_grass.json`
* `tall_grass.json`
* `torchflower.json`
* `white_tulip.json`
* `wither_rose.json`

### craftable

Adds direct crafting recipes for previously uncraftable vanilla blocks/items, or unique alternative materials.

* `black_dye_from_charcoal.json`
* `black_dye_from_coal.json`
* `blackstone.json`
* `bone_block_from_bone.json`
* `brain_coral_block.json`
* `brown_dye.json`
* `brown_mushroom_block.json`
* `bubble_coral_block.json`
* `calcite.json`
* `chipped_to_anvil.json`
* `cobweb.json`
* `crimson_nylium.json`
* `damage_to_chipped.json`
* `fire_coral_block.json`
* `gilded_blackstone.json`
* `grass_block.json`
* `gravel.json`
* `green_dye.json`
* `horn_coral_block.json`
* `ice.json`
* `mushroom_stem.json`
* `mycelium.json`
* `podzol.json`
* `powder_snow_bucket.json`
* `red_mushroom_block.json`
* `red_sand.json`
* `red_sandstone.json`
* `shroomlight.json`
* `snow_block.json`
* `soul_sand.json`
* `trident.json`
* `tube_coral_block.json`
* `tuff.json`
* `warped_nylium.json`

### universal_dyeing

Enables changing colors dynamically between various blocks (concrete, stained glass, terracotta, etc.) using dyes.

* Covers all 16 color variants for:
* `concrete` (e.g., `black_concrete.json` through `yellow_concrete.json`)
* `concrete_powder`
* `stained_glass`
* `stained_glass_pane`
* `terracotta`

### unpackable

Allows players to break down block forms back into their base constituent items (e.g., Amethyst Shards, Clay Balls, Glowstone Dust).

* `amethyst_shard.json`
* `brown_mushroom.json`
* `clay_ball.json`
* `glowstone_dust.json`
* `ice.json`
* `magma_cream.json`
* `nether_wart.json`
* `packed_ice.json`
* `pointed_dripstone.json`
* `quartz.json`
* `red_mushrom.json`
* `snowball.json`
* `string.json`

---

## 5. Minecraft Namespace (`minecraft`)

The `minecraft` folder modifies baseline vanilla parameters (such as increasing stair outputs to match modern recipe standards or adding comprehensive wood stripping alternatives).

* `acacia_stairs.json`
* `acacia_trapdoor.json`
* `acacia_wood.json`
* `andesite_stairs.json`
* `bamboo_mosaic_stairs.json`
* `bamboo_stairs.json`
* `bamboo_trapdoor.json`
* `birch_stairs.json`
* `birch_trapdoor.json`
* `birch_wood.json`
* `blackstone_stairs.json`
* `bricks.json`
* `bricks_stairs.json`
* `cherry_stairs.json`
* `cherry_trapdoor.json`
* `cherry_wood.json`
* `cobbled_deepslate_stairs.json`
* `cobblestone_stairs.json`
* `crimson_hyphae.json`
* `crimson_stairs.json`
* `crimson_trapdoor.json`
* `cut_copper_stairs.json`
* `dark_oak_stairs.json`
* `dark_oak_trapdoor.json`
* `dark_oak_wood.json`
* `dark_prismarine_stairs.json`
* `deepslate_bricks_stairs.json`
* `deepslate_tile_stairs.json`
* `diorite_stairs.json`
* `end_stone_brick_stairs.json`
* `exposed_cut_copper_stairs.json`
* `fermented_spider_eye.json`
* `granite_stairs.json`
* `jungle_stairs.json`
* `jungle_trapdoor.json`
* `jungle_wood.json`
* `mangrove_stairs.json`
* `mangrove_trapdoor.json`
* `mangrove_wood.json`
* `mossy_cobblestone_stairs.json`
* `mossy_stone_brick_stairs.json`
* `mud_brick_stairs.json`
* `nether_brick_stairs.json`
* `nether_brick.json`
* `oak_stairs.json`
* `oak_trapdoor.json`
* `oak_wood.json`
* `oxidized_cut_copper_stairs.json`
* `pale_aok_trapdoor.json`
* `pale_oak_stairs.json`
* `pale_oak_wood.json`
* `polished_andesite_stairs.json`
* `polished_blackstone_brick_stairs.json`
* `polished_blackstone_stairs.json`
* `polished_deepslate_stairs.json`
* `polished_diorite_stairs.json`
* `polished_granite_stairs.json`
* `polished_tuff_stairs.json`
* `powered_rail.json`
* `prismarine_brick_stairs.json`
* `prismarine_stairs.json`
* `purpur_stairs.json`
* `quartz_stairs.json`
* `red_nether_brick_stairs.json`
* `red_nether_bricks.json`
* `red_sandstone_stairs.json`
* `red_sandstone.json`
* `resin_brick_stairs.json`
* `resin_bricks.json`
* `sandstone_stairs.json`
* `sandstone.json`
* `smooth_quartz_stairs.json`
* `smooth_red_sandstone_stairs.json`
* `smooth_sandstone_stairs.json`
* `spruce_stairs.json`
* `spruce_trapdoor.json`
* `spruce_wood.json`
* `sticky_piston.json`
* `stone_brick_stairs.json`
* `stone_stairs.json`
* `stripped_acacia_wood.json`
* `stripped_birch_wood.json`
* `stripped_cherry_wood.json`
* `stripped_crimson_hyphae.json`
* `stripped_dark_oak_wood.json`
* `stripped_jungle_wood.json`
* `stripped_mangrove_wood.json`
* `stripped_oak_wood.json`
* `stripped_pale_oak_wood.json`
* `stripped_spruce_wood.json`
* `stripped_warped_hyphae.json`
* `tuff_brick_stairs.json`
* `tuff_stairs.json`
* `warped_hyphae.json`
* `warped_stairs.json`
* `warped_trapdoor.json`
* `waxed_cut_copper_stairs.json`
* `waxed_exposed_cut_copper_stairs.json`
* `waxed_oxidized_cut_copper_stairs.json`
* `waxed_weathered_cut_copper_stairs.json`
* `weathered_cut_copper_stairs.json`

---

## 6. Recipe Distribution Summary

| Namespace     | Category / Subfolder      | Focus Area                                        | File Count    |
| ---           | ---                       | ---                                               | ---           |
| **Custom**    | `back_to_blocks`          | Un-crafting blocks from components                | 114           |
| **Custom**    | `botanical_replication`   | Plant and flower replication mechanics            | 24            |
| **Custom**    | `craftable`               | Crafting previously un-craftable vanilla items    | 33            |
| **Custom**    | `stonecutter`             | Stonecutter support expansion                     | 8             |
| **Custom**    | `universal_dyeing`        | Dynamic block re-dyeing mechanics                 | 80            |
| **Custom**    | `unpackable`              | Deconstructing unified items into materials       | 13            |
| **Minecraft** | `recipe`                  | Optimization/adjustments to vanilla values        | 103           |
| **Total**     |                           |                                                   | **375**       |
| """           |                           |                                                   |               |
