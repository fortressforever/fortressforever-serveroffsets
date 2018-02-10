# quick hack to just keep track of function vtable offset by addr in rdata
# cffplayer_vtable is made from ida rdata dump of *WINDOWS* binary
# dumps em out in offset# for sourcemod

with open("cffplayer_offsets.txt", "w") as of:
    with open("cffplayer_vtable_v2.7.6.txt") as f:
        lns = f.readlines()

        for i in range(0, len(lns)):
            if i == 0:
                print "0 CFFPlayer::~CFFPlayer"
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
