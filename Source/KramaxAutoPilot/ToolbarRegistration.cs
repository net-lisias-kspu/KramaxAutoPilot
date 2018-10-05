using UnityEngine;
using ToolbarControl_NS;

namespace Kramax
{
    [KSPAddon(KSPAddon.Startup.MainMenu, true)]
    public class RegisterToolbar : MonoBehaviour
    {
		public void Awake()
        {
            ToolbarControl.RegisterMod(Kramax.Toolbar.AppLauncherAutoPilot.MODID, Kramax.Toolbar.AppLauncherAutoPilot.MODNAME);
        }
    }
}