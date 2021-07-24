# Spack Pre-req

This is a [spack extension](https://spack.readthedocs.io/en/latest/extensions.html)
that can be used to determine if you have all system dependencies installed for spack!
You should first add the extension to your spack config. For example, this is in
my `etc/spack/default/config.yaml`:

```yaml
config:
  extensions:
  - /home/vanessa/Desktop/Code/spack-prereq
```

Then you can use it with spack! The default will have a failing return code if
you are missing something:

```bash
$ spack prereq
==> SPACK PRE-REQ INVENTORY
wget                 [X]
bzip2                [X]
tar                  [X]
python               [X]
patch                [X]
curl                 [X]
gzip                 [X]
xz                   [X]
zstd                 [X]
file                 [X]
git                  [X]
hg                   [ ]
svn                  [ ]
c/c++ compiler       [X]
```

Here is the ruhroh return code:

```bash
$ echo $?
1
```

Unless you ask for a force pass.

```bash
spack prereq --force-pass
==> SPACK PRE-REQ INVENTORY
wget                 [X]
bzip2                [X]
tar                  [X]
python               [X]
patch                [X]
curl                 [X]
gzip                 [X]
xz                   [X]
zstd                 [X]
file                 [X]
git                  [X]
hg                   [ ]
svn                  [ ]
c/c++ compiler       [X]
```
And then you get a passing return code anyway!

```bash
$ echo $?
0
```

You can easily customize the script in [prereq](prereq/cmd/prereq.py) to change your
list of dependencies, or check for other things. Here is a terminal demo so you can
see the colors:

[![asciicast](https://asciinema.org/a/426954.svg)](https://asciinema.org/a/426954?speed=2)

Have fun!


## Ways to make this better

Please open a PR to make this better! It's pretty darn simple.

1. Add tests.
2. Print the c/c++ compiler found
3. Check the version of Python is compatible
4. Something else super creative!
