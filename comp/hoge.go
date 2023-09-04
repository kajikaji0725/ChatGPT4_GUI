package comp

import (
	"context"
	"fmt"
)

type Hoge struct {
	ctx context.Context
}

// Greet returns a greeting for the given name
func (a *Hoge) Greet(name string) string {
	return fmt.Sprintf("Hello %s, It's show time!", name)
}