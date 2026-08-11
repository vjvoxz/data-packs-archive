# Crafting Quality of Life: Minecraft Recipes
This file contains JSON files that define the recipes for Minecraft Java Edition 26.3.

## Andesite
```json
{
	"type": "minecraft:crafting_shapeless",
	"group": "andesite",
	"category": "building",
	"ingredients": [
		"minecraft:diorite",
		"minecraft:cobblestone"
	],
	"result": {
		"count": 2,
		"id": "minecraft:andesite"
	}
}
```
## Bone Block
```json
{
	"type": "minecraft:crafting_shaped",
    "group": "boneblock",
	"category": "building",
	"key": {
		"#": "minecraft:bone_meal"
	},
	"pattern": [
		"###",
		"###",
		"###"
	],
	"result": {
		"id": "minecraft:bone_block"
	}
}
```
## Fermented Spider Eye (New Recipe for 26.3)
```json
{
	"type": "minecraft:crafting_shapeless",
	"category": "misc",
	"ingredients": [
		"minecraft:spider_eye",
		"#minecraft:mushrooms",
		"minecraft:sugar"
	],
	"result": {
		"id": "minecraft:fermented_spider_eye"
	}
}
```
## Fermented Spider Eye (Old Recipe)
```json
{
	"type": "minecraft:crafting_shapeless",
	"category": "misc",
	"ingredients": [
	"minecraft:spider_eye",
	[
		"minecraft:brown_mushroom",
		"minecraft:red_mushroom"
	],
	"minecraft:sugar"
	],
	"result": {
	"count": 1,
	"id": "minecraft:fermented_spider_eye"
	}
}
```
## Packed Ice
```json
{
	"type": "minecraft:crafting_shapeless",
	"group": "packed_ice",
	"category": "building",
	"ingredients": [
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice",
		"minecraft:ice"
	],
	"result": {
		"id": "minecraft:packed_ice"
	}
}
```
## Sticky Piston
```json
{
	"type": "minecraft:crafting_shaped",
	"category": "redstone",
	"key": {
		"P": "minecraft:piston",
		"S": [
			"minecraft:slime_ball",
			"minecraft:honeycomb"
		]
	},
	"pattern": [
		"S",
		"P"
	],
	"result": {
		"count": 1,
		"id": "minecraft:sticky_piston"
	}
}
```