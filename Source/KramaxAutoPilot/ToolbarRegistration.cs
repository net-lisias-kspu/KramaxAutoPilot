using UnityEngine;
using KSP.UI.Screens;

using ToolbarControl_NS;

namespace Kramax
{
	using Asset = KSPe.IO.File<KramaxAutoPilot>.Asset;

    [KSPAddon(KSPAddon.Startup.MainMenu, true)]
    public class RegisterToolbar : MonoBehaviour
    {
        internal const string MODID = "Kramax";
        internal const string MODNAME = "Kramax Autopilot";
        internal static ToolbarControl toolbarControl;

		public void Awake()
        {
            ToolbarControl.RegisterMod(MODID, MODNAME);
        }
        
        public static void register_toolbar(GameObject gameObject)
		{
            toolbarControl = gameObject.AddComponent<ToolbarControl>();
            toolbarControl.AddToAllToolbars(
                OnToggleTrue, OnToggleFalse,
                ApplicationLauncher.AppScenes.SPACECENTER |
                ApplicationLauncher.AppScenes.TRACKSTATION |
                ApplicationLauncher.AppScenes.FLIGHT |
                ApplicationLauncher.AppScenes.MAPVIEW,
                MODID,
                MODID + "Button",
                Asset.Solve("Icon", "icon-38"),
                Asset.Solve("Icon", "icon-24"),
                MODNAME
            );

		}

        public static void OnDestroy()
        {
            if (null == toolbarControl) return;
            
            toolbarControl.OnDestroy();
            UnityEngine.Object.Destroy(toolbarControl);
        }
        
		public static void setBtnState(bool state, bool click = false)
        {
            if (null == toolbarControl) return;

            if (state)
                toolbarControl.SetTrue(click);
            else
                toolbarControl.SetFalse(click);
        }

        private static void OnToggleTrue()
        {
            KramaxAutoPilot.bDisplayAutoPilot = true;
        }

        private static void OnToggleFalse()
        {
            KramaxAutoPilot.bDisplayAutoPilot = false;
        }

	}
}