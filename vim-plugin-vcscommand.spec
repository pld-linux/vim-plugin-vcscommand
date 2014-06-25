Summary:	CVS/SVN/SVK/Git/Mercurial integration plugin
Name:		vim-plugin-vcscommand
Version:	1.99.47
Release:	0.1
License:	Distributable
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php?src_id=19809&/vcscommand-%{version}.zip
# Source0-md5:	861c4e1a38664a19ce561527b9b94344
URL:		http://www.vim.org/scripts/script.php?script_id=90
BuildRequires:	unzip
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
VIM 7 plugin useful for manipulating files controlled by CVS, SVN,
SVK, Git, Mercurial within VIM, including committing changes and
performings diffs using the vimdiff system.

To enable this plugin define "use_vcscommand" variable somewhere in
your .vimrc file.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a plugin syntax doc $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%postun
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%files
%defattr(644,root,root,755)
%doc %{_vimdatadir}/doc/vcscommand.txt
%{_vimdatadir}/plugin/vcscommand.vim
%{_vimdatadir}/plugin/vcsbzr.vim
%{_vimdatadir}/plugin/vcscvs.vim
%{_vimdatadir}/plugin/vcsgit.vim
%{_vimdatadir}/plugin/vcshg.vim
%{_vimdatadir}/plugin/vcssvk.vim
%{_vimdatadir}/plugin/vcssvn.vim
%{_vimdatadir}/syntax/vcscommit.vim
%{_vimdatadir}/syntax/cvsannotate.vim
%{_vimdatadir}/syntax/gitannotate.vim
%{_vimdatadir}/syntax/hgannotate.vim
%{_vimdatadir}/syntax/svkannotate.vim
%{_vimdatadir}/syntax/svnannotate.vim
