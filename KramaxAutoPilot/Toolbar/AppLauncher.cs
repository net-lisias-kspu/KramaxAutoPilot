using System;
using System.Collections;
using UnityEngine;
using KSP.UI.Screens;

using ToolbarControl_NS;

namespace Kramax.Toolbar
{
    using Utility;

    public static class AppLauncherAutoPilot
    {
        //private static ApplicationLauncherButton btnLauncher;
        static ToolbarControl toolbarControl;

        public static void Awake()
        {
        }

        internal const string MODID = "Kramax_NS";
        internal const string MODNAME = "Kramax Autopilot";

        public static void Start(GameObject gameObject)
        {
#if false
            if (btnLauncher == null)
                btnLauncher =
                    ApplicationLauncher.Instance.AddModApplication(OnToggleTrue, OnToggleFalse, null, null, null, null,
                                        ApplicationLauncher.AppScenes.FLIGHT, 
                                        GameDatabase.Instance.GetTexture("KramaxAutoPilot/Icon/AppLauncherIcon", false));
#endif
            toolbarControl = gameObject.AddComponent<ToolbarControl>();
            toolbarControl.AddToAllToolbars(OnToggleTrue, OnToggleFalse,
                ApplicationLauncher.AppScenes.SPACECENTER |
                ApplicationLauncher.AppScenes.TRACKSTATION |
                ApplicationLauncher.AppScenes.FLIGHT |
                ApplicationLauncher.AppScenes.MAPVIEW,
                MODID,
                "kramaxButton",
                "KramaxAutoPilot/Icon/icon-38",
                "KramaxAutoPilot/Icon/icon-24",
                MODNAME
            );


        }

        private static void OnToggleTrue()
        {
            KramaxAutoPilot.bDisplayAutoPilot = true;
        }

        private static void OnToggleFalse()
        {
            KramaxAutoPilot.bDisplayAutoPilot = false;
        }

        public static void setBtnState(bool state, bool click = false)
        {
            if (state)
                toolbarControl.SetTrue(click);
            else
                toolbarControl.SetFalse(click);
        }

        public static void OnDestroy()
        {
#if false
            if (btnLauncher != null)
            {
                ApplicationLauncher.Instance.RemoveModApplication(btnLauncher);
                btnLauncher = null;
            }
#endif
            if (toolbarControl != null)
            {
                toolbarControl.OnDestroy();
                UnityEngine.Object.Destroy(toolbarControl);
            }
        }
    }
}
