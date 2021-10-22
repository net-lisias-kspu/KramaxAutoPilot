using System.Collections.Generic;

namespace Kramax
{
	public static class ModuleManagerSupport
	{
		public static IEnumerable<string> ModuleManagerAddToModList()
		{
			string[] r = {Version.Namespace};
			return r;
		}
	}
}
