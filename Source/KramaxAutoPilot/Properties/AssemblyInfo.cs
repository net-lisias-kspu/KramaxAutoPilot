using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
[assembly: AssemblyTitle("KramaxAutoPilot /L Unofficial")]
[assembly: AssemblyDescription("Course guidance and auto-land for spaceplanes")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany(Kramax.LegalMamboJambo.Company)]
[assembly: AssemblyProduct(Kramax.LegalMamboJambo.Product)]
[assembly: AssemblyCopyright(Kramax.LegalMamboJambo.Copyright)]
[assembly: AssemblyTrademark(Kramax.LegalMamboJambo.Trademark)]
[assembly: AssemblyCulture("")]

// Setting ComVisible to false makes the types in this assembly not visible 
// to COM components.  If you need to access a type in this assembly from 
// COM, set the ComVisible attribute to true on that type.
[assembly: ComVisible(false)]

// The following GUID is for the ID of the typelib if this project is exposed to COM
[assembly: Guid("138C7DA7-7043-429C-B204-0F705D867791")]

// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Build and Revision Numbers 
// by using the '*' as shown below:
// [assembly: AssemblyVersion("1.0.*")]
//[assembly: AssemblyVersion("1.0.0.*")]
[assembly: AssemblyFileVersion(Kramax.Version.Number)]
[assembly: AssemblyVersion(Kramax.Version.Number)]
[assembly: KSPAssembly("KramaxAutoPilot", Kramax.Version.major, Kramax.Version.minor)]

[assembly: KSPAssemblyDependency("KSPe", 2, 4)]
[assembly: KSPAssemblyDependency("KSPe.UI", 2, 4)]
