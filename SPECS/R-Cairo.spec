%global packname  Cairo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.9
Release:          1%{?dist}
Summary:          R graphics device using cairo graphics library for creating high-quality bitmap (PNG, JPEG, TIFF), vector (PDF, SVG, PostScript) and display (X11 and Win32) output

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-grDevices R-graphics
# Suggests:  R-png
# LinkingTo:
# Enhances:



Requires:         R-grDevices R-graphics
Requires:         R-png
BuildRequires:    R-devel tex(latex)
BuildRequires:    R-grDevices R-graphics
BuildRequires:    R-png
BuildRequires:    cairo-devel libX11-devel libXt-devel

%description
Cairo graphics device that can be use to create high-quality vector (PDF,
PostScript and SVG) and bitmap output (PNG,JPEG,TIFF), and high-quality
rendering in displays (X11 and Win32). Since it uses the same back-end for
all output, copying across formats is WYSIWYG. Files are created without
the dependence on X11 or other external programs. This device supports
alpha channel (semi-transparent drawing) and resulting images can contain
transparent and semi-transparent regions. It is ideal for use in server
environments (file output) and as a replacement for other devices that
don't have Cairo's capabilities such as alpha support or anti-aliasing.
Backends are modular such that any subset of backends is supported.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 1.5.9-1
- initial package for Fedora
