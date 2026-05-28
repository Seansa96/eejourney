Tags: [[Weakauras]] [[WoW API]] 

First, we need a trigger. The simplest way to accomplish the goal of this Weakaura is just to use the "**ZONE_CHANGED_NEW_AREA*" event, which happens when a player loads a new map (basically enters a new area and goes to loading screen).

Entering dungeons and raids pretty much guarantees this event.  Next, we'll want to check if we're actually in an instance.  There's a specific function available for this, called `IsInInstance()`, note the case.

This function returns two things, a boolean detailing whether or not the unit is in an instance (value of true or false accordingly), and the instance type the unit is in, if the first value is true.  5 man content has a value of "party", so we just need to do a simple check to see if we're in an instance, and if the instance type is a dungeon, or "party"

```
function(event)
local inInstance, instanceType = IsInstance()

if inInstance and (instanceType == "party")
then
return true
	end
end
```

This will be our custom trigger function, and it pretty much accomplishes what we need. Not particularly elegant, but works.

Now, since we want to show the name of the current loadout (and save ourselves a click), we just need to include the name of our current talent loadout. Unfortunately, the way to obtain that is a little convoluted, but still achievable fairly quickly.

Just change the text display to whatever you want, and accompany that with a nice `%c` for the custom display function.

Now, let's get the talent loadout name.

There's a couple of CVars we'll have to go through to get that.

The name is contained within the table returned to us by **C_Traits.GetConfigInfo().** This needs the configID for the loadout we want further details on, and can be accessed via the dot operator.

Ex:

```
local config = C_Traits.GetConfigInfo(configID)
return config.name
```
This would return the name of the loadout, which is what we want. But, we're working backwards, so there's to more steps to even get here.

We need the config ID, which is obtained from the 

**C_ClassTalents.GetLastSelectedSavedConfigID()** function. This function needs a **specID** to return a value, that being the config ID. We can finally get that specID from **PlayerUtil.GetCurrentSpecID()**.

So, all in all, it should look something like:

```
function()
    local specID = PlayerUtil.GetCurrentSpecID()
    local loadoutID = C_ClassTalents.GetLastSelectedSavedConfigID(specID)
    local config = C_Traits.GetConfigInfo(loadoutID)
    
    if loadoutID then
        return config.name
    else
        return "No active loadout"
    end
end
```

	And that should get it to work. For the TTS portion, just refer to [[Making a TTS Weakaura]].