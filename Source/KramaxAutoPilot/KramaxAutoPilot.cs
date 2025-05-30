﻿/*
 * SimplePartlessPlugin.cs
 * 
 * Part of the KSP modding examples from Thunder Aerospace Corporation.
 * 
 * (C) Copyright 2013, Taranis Elsu
 * 
 * Kerbal Space Program is Copyright (C) 2013 Squad. See http://kerbalspaceprogram.com/. This
 * project is in no way associated with nor endorsed by Squad.
 * 
 * This code is licensed under the Apache License Version 2.0. See the LICENSE.txt and NOTICE.txt
 * files for more information.
 * 
 * Note that Thunder Aerospace Corporation is a ficticious entity created for entertainment
 * purposes. It is in no way meant to represent a real entity. Any similarity to a real entity
 * is purely coincidental.
 */

#if DEBUG
//TODO: Redirect this to the debugging version of the reloader.
using MonoBehaviour = KramaxReloadExtensions.ReloadableMonoBehaviour;
#else
using MonoBehaviour = KramaxReloadExtensions.ReloadableMonoBehaviour;
#endif

using GUI = KSPe.UI.GUI;
using GUILayout = KSPe.UI.GUILayout;

namespace Kramax
{
    using Utility;

    /*
     * This project is meant to be a "Hello World" example showing how to make a part-less plugin.
     * 
     * The main class for your plug-in should implement MonoBehavior, which is a Unity class.
     * http://docs.unity3d.com/Documentation/ScriptReference/MonoBehaviour.html
     * 
     * KSPAddon is an "attribute" that lets KSP know that this class is a plug-in. KSP will create
     * an instance of the class whenever the game loads the specified scene. The second parameter
     * tells KSP whether to create an instance once, or every time it loads the scene.
     * 
     * Do not use true for the second parameter until this bug gets fixed:
     * http://forum.kerbalspaceprogram.com/threads/45107-KSPAddon-bug-causes-mod-incompatibilities
     * That link has a workaround, but prefer to use false unless your needs dictate otherwise.
     * 
     * The lifecycle for KSP comes from Unity with a few differences:
     *    
     *    Constructor -> Awake() -> Start() -> Update/FixedUpdate() [repeats] -> OnDestroy()
     * 
     * When the specified game scene loads, first KSP will construct your MonoBehaviour class and
     * call Awake(). When it finishes doing that for all the mods, then it calls Start(). After
     * that, it will call Update() every frame and FixedUpdate() every physics time step. Just
     * before exiting the scene, the game will call OnDestroy() which gives you the opportunity to
     * save any settings.
     * 
     * Unity uses Serialization a lot, so use the Awake() method to initialize your fields rather
     * than the constructor. And you can use OnDestroy() to do some of the things you would do in
     * a destructor.
     * 
     * Also see http://www.richardfine.co.uk/2012/10/unity3d-monobehaviour-lifecycle/ for more
     * information about the Unity lifecycle.
     * 
     * This plugin does not actually do anything beyond logging to the Debug console, which you
     * can access by pressing Alt+F2 or Alt+F12 (on Windows, for OSX use Opt and for Linux use
     * Right Shift). You can also look at the debug file, which you can find at
     * {KSP}/KSP_Data/output_log.txt.
     */
    [KSPAddon(KSPAddon.Startup.Flight, false)]
	public class KramaxAutoPilot : MonoBehaviour
    {
		private readonly bool bUseStockToolbar = true;
        public static bool bDisplayAutoPilot = false; // set by launcher
        public static bool bDisplayTooltips = true; // set by launcher
        public static bool bHideUI = false;
		private George mainPilot = null;

         /*
         * Caution: as it says here: http://docs.unity3d.com/Documentation/ScriptReference/MonoBehaviour.Awake.html,
         * use the Awake() method instead of the constructor for initializing data because Unity uses
         * Serialization a lot.
         */
        public KramaxAutoPilot()
        {
            Log.detail("KramaxAutoPilot: ctor {0}", this.GetInstanceID());
        }

        /*
         * Called after the scene is loaded.
         */
        public void Awake()
        {
            Log.detail("KramaxAutoPilot: Awake {0}", this.GetInstanceID());
            ToolbarController.register_toolbar(gameObject);
        }

        private bool UseAppLauncher()
        {
            return bUseStockToolbar /* || !Kramax.Toolbar.ToolbarManager.ToolbarAvailable */;
        }

        /*
         * Called next.
         */
        public void Start()
        {
			Log.detail("KramaxAutoPilot: Start {0}", this.GetInstanceID()); 
          
            // read in config
            // initialize any variables
            // install any callbacks
            // install in toolbar

            if (mainPilot != null)
            {
                Log.error("KramaxAutoPilot.Start: mainPilot stil exists");
            }
            else
            {
                Log.detail("KramaxAutoPilot.Start: creating mainPilot");
                mainPilot = AddComponent(typeof(George)) as George;
            }
        }

        /*
         * Called every frame
         */
        public void Update()
        {
            // Deb.Verb("KramaxAutoPilot: Update");
            if (UseAppLauncher())
            {
                // Not needed. KSPe.Toolbar handles the mess itself.
                //Kramax.RegisterToolbar.setBtnState(bDisplayAutoPilot);
             
            }
        }

        /*
         * Called at a fixed time interval determined by the physics time step.
         */
        public void FixedUpdate()
        {
            // Deb.Verb("KramaxAutoPilot: FixedUpdate");
        }

        public void LateUpdate()
        {
            // Deb.Verb("KramaxAutoPilot: LateUpdate");
        }

		/*
        public void OnGUI()
        {
            if (GeneralUI.UISkin == null)
                GeneralUI.customSkin();

            if (bHideUI)
                return;

            GUI.skin = GeneralUI.UISkin;
            GUI.backgroundColor = GeneralUI.stockBackgroundGUIColor;
            Draw();
        }

        public void Draw()
        {
            if (bDisplayOptions)
                window = ClickThruBlocker.GUILayoutWindow(0984653, window, optionsWindow, "", GUILayout.Width(0), GUILayout.Height(0));
        }

       
        private void optionsWindow(int id)
        {
            if (GUI.Button(new Rect(window.width - 16, 2, 14, 14), ""))
                bDisplayOptions = false;

            bDisplayAutoPilot = GUILayout.Toggle(bDisplayAutoPilot, "Kramax Autopilot", GeneralUI.UISkin.customStyles[(int)myStyles.btnToggle]);

            if (GUILayout.Button("Update Defaults"))
            {
                PresetManager.updateDefaults();
            }

            if (controlledVessels.Count > 1)
            {
                GUILayout.BeginHorizontal();
                for (int i = 0; i < controlledVessels.Count; i++)
                {
                    if (controlledVessels[i].vesselRef.isActiveVessel)
                        GUI.backgroundColor = Color.green;
                    bool tmp = GUILayout.Toggle(i == selectedVesselIndex, i.ToString(), GeneralUI.UISkin.customStyles[(int)myStyles.btnToggle]);
                    if (tmp)
                        selectedVesselIndex = i;
                    GUI.backgroundColor = GeneralUI.stockBackgroundGUIColor;
                }
                GUILayout.EndHorizontal();
            }

            GUI.DragWindow();
        }
        */

		private void hideUI()
        {
            bHideUI = true;
        }

		private void showUI()
        {
            bHideUI = false;
        }
       
        public void OnDestroy()
        {
            Log.detail("KramaxAutoPilot: OnDestroy {0}", this.GetInstanceID());

            if (mainPilot)
            {
                Destroy(mainPilot);
                mainPilot = null;
            }
        }
    }
}
