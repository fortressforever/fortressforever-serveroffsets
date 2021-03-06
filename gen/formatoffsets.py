# quick hack to just keep track of function vtable offset by addr in rdata
# cffplayer_vtable is made from ida rdata dump of *WINDOWS* binary
# dumps em out in offset# for sourcemod

# to generate the input file, search .rdata section in IDA for ~CFFPlayer to
# find the start of the vtable and copy paste it into a file starting with
# the line that is '; const CBasePlayer::`vftable''

IN = "cffplayer_vtable_v2.7.6.txt"
OUT = "cffplayer_offsets.txt"

with open(OUT, "w") as of:
    with open(IN) as f:
        lns = f.readlines()

        for i in range(0, len(lns)):
            if i == 0:
                of.write("0 - CFFPlayer::~CFFPlayer\n")
                continue

            # hack: skip the vtable header lines
            offset = i - 4
            if offset <= 0:
                continue

            # now we got a good line, format it a bit. we can split on spaces and get something
            # usable thankfully!
            chunks = lns[i].split()

            fn = " ".join(chunks[5:])

            outline = "{} - {}\n".format(offset, fn)
            of.write(outline)
            print outline
