---
headerVersion: 2023.11.25
tags: [person, status/needswork/notes]
campaignInfo:
- {campaign: clee}
name: Ysabel
born: 1688
died: 1720-01-06
species: human
ancestry: Sembaran
gender: female
affiliations:
- {org: Lord's Guard of Cleenseau, title: Sheriff}
whereabouts:
- {type: home, location: Cleenseau}
title: Ysabel
hide: [toc]
---

# Ysabel
<div class="grid cards ext-narrow-margin ext-one-column" markdown>
- :octicons-info-24:{ .lg .middle } __Biographical Information__

    A Sembaran [human](<../../species/humans/humans.md>) (she/her)  
    b. DR 1688 - d. January 6th, 1720, died at age 32 years  
    Sheriff of the Lord's Guard of Cleenseau (until January 6th, 1720)  
    { .bio }

    Lived in Cleenseau, the Manor of Cleenseau, the Barony of Aveil
</div>


A striking and comely woman with a rough scar running from her eye to her neck. She is the sheriff of Cleenseau and leads a part of the Lord's Guard. She has many opinions about her employers, in particular Rinault Essford, and does not always successfully keep them to herself.

![[ysabel.png|420]]


### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Alive"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.isAlive(b.file.frontmatter, dv.current().pageTargetDate)]))
```
