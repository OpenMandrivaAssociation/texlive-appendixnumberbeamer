%global tl_name appendixnumberbeamer
%global tl_revision 79061

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	Manage frame numbering in appendixes in beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/appendixnumberbeamer
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendixnumberbeamer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package fixes the frame numbering in beamer when using an appendix
such that the slides from the appendix are not counted in the total
frame number of the main part of the document. The total frame number
counter is reset to 0 when entering the appendix. The standard usage is
to include \usepackage{appendixnumberbeamer} in the preamble and then
declare the beginning of the appendix as usual using the \appendix
command.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/appendixnumberbeamer
%dir %{_datadir}/texmf-dist/tex/latex/appendixnumberbeamer
%doc %{_datadir}/texmf-dist/doc/latex/appendixnumberbeamer/README.md
%doc %{_datadir}/texmf-dist/doc/latex/appendixnumberbeamer/VERSION
%{_datadir}/texmf-dist/tex/latex/appendixnumberbeamer/appendixnumberbeamer.sty
