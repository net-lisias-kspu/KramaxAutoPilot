using UnityEngine;
using KSP.UI.Screens;

using KSPe.Annotations;
using Toolbar = KSPe.UI.Toolbar;
using Asset = KSPe.IO.Asset<Kramax.KramaxAutoPilot>;

namespace Kramax
{
	[KSPAddon(KSPAddon.Startup.MainMenu, true)]
	public class ToolbarController : MonoBehaviour
	{
		internal static KSPe.UI.Toolbar.Toolbar Instance => KSPe.UI.Toolbar.Controller.Instance.Get<ToolbarController>();

		[UsedImplicitly]
		private void Start()
		{
			KSPe.UI.Toolbar.Controller.Instance.Register<ToolbarController>(Version.FriendlyName);
		}

		private static Toolbar.Button button = null;
		internal static void register_toolbar(object gameObject)
		{
			if (null != button) return;
			Instance.Add(
				button = Toolbar.Button.Create(gameObject
					, ApplicationLauncher.AppScenes.SPACECENTER | ApplicationLauncher.AppScenes.TRACKSTATION
						| ApplicationLauncher.AppScenes.FLIGHT | ApplicationLauncher.AppScenes.MAPVIEW
					, Asset.Texture2D.LoadFromFile("Icon", "icon-38")
					, Asset.Texture2D.LoadFromFile("Icon", "icon-24")
				)
			);
			button.Toolbar.Add(Toolbar.Button.ToolbarEvents.Kind.Active, new Toolbar.Button.Event(OnToggleTrue, OnToggleFalse));
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