#define CATCH_CONFIG_MAIN

#include "Catch/single_include/catch2/catch.hpp"

#include "hstrat_recomb_concept/example.hpp"

TEST_CASE("Test example") {
  REQUIRE( hstrat_recomb_concept::example() );
}
