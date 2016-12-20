#include <stdio.h>
#include <zlog.h>

#define ANSI_NORM   "\e[0m"
#define ANSI_NL     "\e[0m\n"
#define ANSI_RED    "\e[31m"
#define ANSI_GREEN  "\e[32m"

int main(int argc, char** argv)
{
    // Initialize zlog by loading config from file with a default category
	if ( dzlog_init("./zlog.conf", "my_cat") )
    {
		printf(ANSI_RED "zlog init failed" ANSI_NL);
		return -1;
	}
    else
    {
        printf(ANSI_GREEN "zlog init succeeded" ANSI_NL);
    }

    // Logging happens with a default category
    dzlog_warn("warn");
    dzlog_info("hello, zlog %d", 5);
    dzlog_error(ANSI_RED "error" ANSI_NORM);

    // De-allocate any resources used by zlog
	zlog_fini();

	return 0;
}
