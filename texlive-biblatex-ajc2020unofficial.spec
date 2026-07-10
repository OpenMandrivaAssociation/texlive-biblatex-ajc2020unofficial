%global tl_name biblatex-ajc2020unofficial
%global tl_revision 54401

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.0
Release:	%{tl_revision}.1
Summary:	BibLaTeX style for the Australasian Journal of Combinatorics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-ajc2020unofficial
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an unofficial BibLaTeX style for the Australasian Journal of
Combinatorics. Note that the journal (as for 01 March 2020) does not
accept BibLaTeX, so you probably want to use biblatex2bibitem.

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
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-ajc2020unofficial
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-ajc2020unofficial
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-ajc2020unofficial/README.md
%{_datadir}/texmf-dist/tex/latex/biblatex-ajc2020unofficial/ajc2020unofficial.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-ajc2020unofficial/ajc2020unofficial.cbx
