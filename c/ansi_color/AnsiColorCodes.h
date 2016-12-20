/*
 * AnsiColorCodes.h
 *
 * This file contains C preprocessor definitions and macros for using ANSI color codes in console
 * and log file output.
 *
 * These codes are supported by pretty much every non-Windows terminal/console application as well
 * as most standard Linux/Unix/POSIX command line utilities such as:
 * - cat
 * - less -r
 * - tail
 * - head
 * - more
 * - grep --color=never
 *
 * They work with pretty much any code construct which sends output to a console or file such as:
 * - LOG_INFO(), etc.
 * - printf()
 * - cout
 * - zlog
 * - etc.
 *
 * Using color can make it radically easier to find a needle in a haystack, particularly when a
 * human is attempting to visually parse a wall of text.
 *
 * Intended us is similar to the following:
 *    #include "AnsiColorCodes.h"
 *    LOG_INFO(ANSI_GREEN("Hello World!"));
 */

#pragma once

// ANSI Codes
#define ANSI_RESET          "\e[0m"     // reset, clears all colors and styles to terminal default
#define ANSI_BOLD           "\e[1m"     // bold on
#define ANSI_ITALICS        "\e[3m"     // italics on
#define ANSI_UNDERLINE      "\e[4m"     // underline on
#define ANSI_INVERSE        "\e[7m"     // inverse on, reverses foreground and background colors
#define ANSI_STRIKE         "\e[9m"     // strikethrough on
#define ANSI_BOLD_OFF       "\e[22m"    // bold off
#define ANSI_ITALICS_OFF    "\e[23m"    // italics off
#define ANSI_UNDERLINE_OFF  "\e[24m"    // underline off
#define ANSI_INVERSE_OFF    "\e[27m"    // inverse off
#define ANSI_STRIKE_OFF     "\e[22m"    // strikethrough off
#define ANSI_FG_BLACK       "\e[30m"    // set foreground color to black
#define ANSI_FG_RED         "\e[31m"    // set foreground color to red
#define ANSI_FG_GREEN       "\e[32m"    // set foreground color to green
#define ANSI_FG_YELLOW      "\e[33m"    // set foreground color to yellow
#define ANSI_FG_BLUE        "\e[34m"    // set foreground color to blue
#define ANSI_FG_MAGENTA     "\e[35m"    // set foreground color to magenta
#define ANSI_FG_CYAN        "\e[36m"    // set foreground color to cyan
#define ANSI_FG_WHITE       "\e[37m"    // set foreground color to white
#define ANSI_FG_DEFAULT     "\e[39m"    // set foreground color to default
#define ANSI_BG_BLACK       "\e[40m"    // set background color to black
#define ANSI_BG_RED         "\e[41m"    // set background color to red
#define ANSI_BG_GREEN       "\e[42m"    // set background color to green
#define ANSI_BG_YELLOW      "\e[43m"    // set background color to yellow
#define ANSI_BG_BLUE        "\e[44m"    // set background color to blue
#define ANSI_BG_MAGENTA     "\e[45m"    // set background color to magenta
#define ANSI_BG_CYAN        "\e[46m"    // set background color to cyan
#define ANSI_BG_WHITE       "\e[47m"    // set background color to white
#define ANSI_BG_DEFAULT     "\e[49m"    // set background color to default

// ANSI Macros which set foreground color at start and reset to "normal" at end
#define ANSI_RESET_NL   "\e[0m\n"
#define ANSI_BLACK(x)   ANSI_FG_BLACK x ANSI_RESET_NL
#define ANSI_RED(x)     ANSI_FG_RED x ANSI_RESET_NL
#define ANSI_GREEN(x)   ANSI_FG_GREEN x ANSI_RESET_NL
#define ANSI_YELLOW(x)  ANSI_FG_YELLOW x ANSI_RESET_NL
#define ANSI_BLUE(x)    ANSI_FG_BLUE x ANSI_RESET_NL
#define ANSI_MAGENTA(x) ANSI_FG_MAGENTA x ANSI_RESET_NL
#define ANSI_CYAN(x)    ANSI_FG_CYAN x ANSI_RESET_NL
#define ANSI_WHITE(x)   ANSI_FG_WHITE x ANSI_RESET_NL

// Same deal but without a newline added after the reset
#define ANSI_BLACK_NL(x)    ANSI_FG_BLACK x ANSI_RESET
#define ANSI_RED_NL(x)      ANSI_FG_RED x ANSI_RESET
#define ANSI_GREEN_NL(x)    ANSI_FG_GREEN x ANSI_RESET
#define ANSI_YELLOW_NL(x)   ANSI_FG_YELLOW x ANSI_RESET
#define ANSI_BLUE_NL(x)     ANSI_FG_BLUE x ANSI_RESET
#define ANSI_MAGENTA_NL(x)  ANSI_FG_MAGENTA x ANSI_RESET
#define ANSI_CYAN_NL(x)     ANSI_FG_CYAN x ANSI_RESET
#define ANSI_WHITE_NL(x)    ANSI_FG_WHITE x ANSI_RESET
