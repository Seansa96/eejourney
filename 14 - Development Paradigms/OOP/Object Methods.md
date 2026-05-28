Tags2025-05-12 00:23

Status: #baby

Tags: [[oop]] [[programming concept]]

# Object Methods


Deciding when to make a new method and what scope it should belong to is generally a case by case decision, but it relies on a few factors you should consider:

1. Does this method make sense to go here?
Say we have some class named `Player.cs`

This is just a basic class with a constructor and some attributes set on instantiation, and has a simple method TakeDamage() that accepts an int value for the damage dealt to the Player and then reduces the private int Health by that amount.

If we wanted to add a new method GetPlayerName, it *could* go in the Player Class, sure. It sort of works, and for every player we'd have a way to access their name pretty easily, but is that the best fit for it?

In a lot of cases, yes, it is. Either that, or we'd just access the property directly without the use of an additional method.  

2. DRY and maintainable

Age old checklist. See if creating this method will reduce repetitive calls (like fitting nicely in a loop or being a good callback function or something similar).




## Reference:
