---
layout: page
title: "integrating gui toolkits with rtcs"
---

<!-- Title: Integrating GUI Toolkits with RTCs -->
#contents

## Introduction

The GUI joystick included as a Python sample is one example: <br>
[TkJoyStickComp.py](http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/TkJoyStick/TkJoyStickComp.py)

Another example is the simple mobile robot simulator sample: <br>
[TkMobileRobotSimulator.py](http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/MobileRobotCanvas/TkMobileRobotSimulator.py)

## Example of TkJoystickComp

The `main` function in the TkJoystickComp sample is as follows:

```

def main():
tkJoyCanvas = tkjoystick.TkJoystick() # Create a GUI object
tkJoyCanvas.master.title("TkJoystick")
mgr = OpenRTM_aist.Manager.init(sys.argv) # Create the RTC manager
mgr.activateManager() # Activate the manager

# Register the component

profile = OpenRTM_aist.Properties(defaults_str=tkjoystick_spec)
mgr.registerFactory(profile,
TkJoyStick,
OpenRTM_aist.Delete)

# Create the component

comp = mgr.createComponent("TkJoyStick")

# This component has a member function called set_pos,

# which is used to pass the GUI joystick coordinates to the component.

# Set it as a callback so that it is called when

# the TkJoystick GUI update event is invoked.

tkJoyCanvas.set_on_update(comp.set_pos)
mgr.runManager(True) # Start the manager in non-blocking mode by passing True to runManager
tkJoyCanvas.mainloop() # Enter the Python GUI main loop.

if **name** == "**main**":
main()

```

## Key Points

### It is safer not to call GUI main loop functions or create GUI objects from within a component

Some GUI toolkits include functions that must be called from the main thread, or that assume they are always called from the same thread.

In RTCs, the thread that calls `onInitialize` / `onFinalize` is different from the thread that calls `onExecute`, `onActivated`, `onDeactivated`, and other callbacks. In addition, functions such as `onExecute` may even be called concurrently from multiple threads.

Treating the GUI thread and RTC separately is likely to avoid many problems.

### Exchange data between the GUI and RTC by adding dedicated functions to the RTC

- For the reasons described above, it is better to separate the GUI from the component. However, this can be inconvenient when data must be exchanged between the GUI and the RTC. Usually, an additional interface for data exchange is inherited by the RTC, and the pointer to the component obtained by `createComponent` is used so that the GUI can get or set data.

```

class IMyInterface
{
public:
virtual int getData() = 0;
virtual void setData(double x, double y) = 0;
};

class MyComponent
: public IMyInterface,
public RTC::DataFlowComponentBase
{
: Component definition
public:
virtual int getData()
{
coil::Guard guard(m_outdatalock);
return m_outdata;
}
virtual void setData(double x, double y)
{
coil::Guard guard(m_indatalock);
m_indata.x = x;
m_indata.y = y;
}
};

```

After implementing the component in this way:

```

RTObject_impl* rtobj = mgr.createComponent("MyComponent");
IMyInterface* comp = dynamic_cast<IMyInterface*>(rtobj);
if (comp == 0) { abort(); }
mgr.runManager(true);
gui.mainloop();

```

Then, within the GUI controls, exchange data with the RTC as follows:

```

std::cout << "out data: " << comp->getData() << std::endl; // Get data
comp->setData(1.0, 2.0); // Input data

```

### It is easier to understand if RTCs and GUI controls or widgets correspond one-to-one

However, GUI controls and RTCs are created in different ways. Therefore, it is better to create them separately and associate the GUI controls with the RTC through the data input/output functions implemented in the RTC, as described above.

In the simple mobile robot simulator sample, mobile robot objects and their corresponding RTCs are dynamically added and removed.<br>
[TkMobileRobotSimulator.py](http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/MobileRobotCanvas/TkMobileRobotSimulator.py)
