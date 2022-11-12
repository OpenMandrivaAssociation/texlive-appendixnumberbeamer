Name:		texlive-appendixnumberbeamer
Version:	46317
Release:	1
Summary:	Manage frame numbering in appendixes in beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/appendixnumberbeamer
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package arranges that an appendix in a beamer presentation
is not counted in the frame count of the presentation;
appendixes are numbered starting from one.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/appendixnumberbeamer
%doc %{_texmfdistdir}/doc/latex/appendixnumberbeamer

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
