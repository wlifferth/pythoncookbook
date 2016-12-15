expr -> term + expr
expr -> term
term -> term * factor
term -> factor
factor -> ( expr )
factor -> const
const -> integer

So 3 * 7 is a valid expression because:
expr -> term
term -> term * factor
term * factor -> factor * factor
factor -> const so 
factor * factor -> const * const
const -> integer
3 * 7
