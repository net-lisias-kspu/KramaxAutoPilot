using UnityEngine;
using ToolbarControl_NS;

namespace Kramax
{
    [KSPAddon(KSPAddon.Startup.MainMenu, true)]
    public class RegisterToolbar : MonoBehaviour
    {
        void Start()
        {
            ToolbarControl.RegisterMod(Kramax.Toolbar.AppLauncherAutoPilot.MODID, Kramax.Toolbar.AppLauncherAutoPilot.MODNAME);
        }
    }
}