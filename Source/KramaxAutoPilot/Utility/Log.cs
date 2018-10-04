using System;
using KSPe;
using KSPe.Util.Log;

namespace Kramax.Utility
{
	public static class Deb
	{
		private static Logger logger = new UnityLogger("KRAMAX");
		public static bool debug { 
			get => logger.level > Level.INFO; 
			set => logger.level = debug ? Level.TRACE : Level.INFO;
		}

		public static void Log(String format, params System.Object[] args)
        {
            logger.detail(format, args);
        }

        public static void Log(String message)
        {
            logger.trace(message);
        }

        public static void Verb(String format, params System.Object[] args)
        {
            logger.detail(format, args);
        }

        public static void Verb(String message)
        {
            logger.detail(message);
        }

        public static void Err(String format, params System.Object[] args)
        {
            logger.error(format, args);
        }
	}
}
