<!-- source: https://ui.nuxt.com/components/page-card --> # PageCardPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageCard.vue)

A pre-styled card component that displays a title, description and optional
link.

## Usage

The PageCard component provides a flexible way to display content in a card
with an illustration in the default slot.

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

![Tailwind CSS](/tailwindcss-v4.svg)

Use the [PageGrid](/components/page-grid), [PageColumns](/components/page-
columns) or [PageList](/components/page-list) components to display multiple
PageCard.

### Title

Use the `title` prop to set the title of the card.

title

Tailwind CSS

    
    
    <template>
      <UPageCard title="Tailwind CSS" />
    </template>
    

### Description

Use the `description` prop to set the description of the card.

description

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
      />
    </template>
    

### Icon

Use the `icon` prop to set the icon of the card.

icon

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
      />
    </template>
    

### Link

You can pass any property from the
[`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component such
as `to`, `target`, `rel`, etc.

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

[](https://tailwindcss.com/docs/v4-beta)

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
        to="https://tailwindcss.com/docs/v4-beta"
        target="_blank"
      />
    </template>
    

### Variant

Use the `variant` prop to change the style of the card.

variant

soft

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

[](https://tailwindcss.com/docs/v4-beta)

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
        to="https://tailwindcss.com/docs/v4-beta"
        target="_blank"
        variant="soft"
      />
    </template>
    

You can apply the `light` or `dark` class to the `links` slot when using the
`solid` variant to reverse the colors.

### Orientation

Use the `orientation` prop to change the orientation with the default slot.
Defaults to `vertical`.

orientation

horizontal

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

![Tailwind CSS](/tailwindcss-v4.svg)

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
        orientation="horizontal"
      >
        <img src="/tailwindcss-v4.svg" alt="Tailwind CSS" class="w-full" />
      </UPageCard>
    </template>
    

### Reverse

Use the `reverse` prop to reverse the orientation of the default slot.

orientation

horizontal

reverse

true

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

![Tailwind CSS](/tailwindcss-v4.svg)

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
        orientation="horizontal"
        reverse
      >
        <img src="/tailwindcss-v4.svg" alt="Tailwind CSS" class="w-full" />
      </UPageCard>
    </template>
    

### Highlight

Use the `highlight` and `highlight-color` props to display a highlighted
border around the card.

highlight

true

highlightColor

primary

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

![Tailwind CSS](/tailwindcss-v4.svg)

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
        orientation="horizontal"
        highlight
        highlight-color="primary"
      >
        <img src="/tailwindcss-v4.svg" alt="Tailwind CSS" class="w-full" />
      </UPageCard>
    </template>
    

### Spotlight

Use the `spotlight` and `spotlight-color` props to display a spotlight effect
that follows your mouse cursor and highlights borders on hover.

The spotlight effect will take over hover effects when using a `to` prop. It's
best to use it with the `outline` variant.

spotlight

true

spotlightColor

primary

Tailwind CSS

Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant
improvements.

![Tailwind CSS](/tailwindcss-v4.svg)

    
    
    <template>
      <UPageCard
        title="Tailwind CSS"
        description="Nuxt UI v3 integrates with latest Tailwind CSS v4, bringing significant improvements."
        icon="i-simple-icons-tailwindcss"
        orientation="horizontal"
        spotlight
        spotlight-color="primary"
      >
        <img src="/tailwindcss-v4.svg" alt="Tailwind CSS" class="w-full" />
      </UPageCard>
    </template>
    

You can also customize the color and size by using the `--spotlight-color` and
`--spotlight-size` CSS variables:

    
    
    <template>
      <UPageCard spotlight class="[--spotlight-color:var(--ui-error)] [--spotlight-size:200px]" />
    </template>
    

## Examples

### As a testimonial

Use the [User](/components/user) component in the `header` or `footer` slot to
make the card look like a testimonial.

“Nuxt on Cloudflare infra with minimal effort - this is huge!”

![Evan You](https://avatars.githubusercontent.com/u/499550?v=4)

Evan You

Author of Vue.js and Vite

    
    
    <script setup lang="ts">
    const testimonial = ref({
      user: {
        name: 'Evan You',
        description: 'Author of Vue.js and Vite',
        avatar: {
          src: 'https://avatars.githubusercontent.com/u/499550?v=4',
          alt: 'Evan You'
        }
      },
      quote: '“Nuxt on Cloudflare infra with minimal effort - this is huge!”'
    })
    </script>
    
    <template>
      <UPageCard :description="testimonial.quote" class="w-60">
        <template #footer>
          <UUser v-bind="testimonial.user" />
        </template>
      </UPageCard>
    </template>
    

[](/components/page-columns)You can use the [`PageColumns`](/components/page-
columns) component to display multiple PageCard in a multi-column layout.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`  
`icon`| | ` string`The icon displayed above the title.  
`reverse`| `false`| `boolean`Reverse the order of the default slot.  
`target`| | ` null | "_blank" | "_parent" | "_self" | "_top" | string & {}`  
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Show properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`title`| | ` string`  
`description`| | ` string`  
`variant`| `'outline'`| ` "solid" | "outline" | "soft" | "subtle" | "ghost" | "naked"`  
`highlight`| | `boolean`Display a line around the page card.  
`highlightColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`spotlight`| | `boolean`Display a spotlight effect that follows your mouse cursor and highlights borders on hover.  
`spotlightColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`ui`| | ` { root?: ClassNameValue; spotlight?: ClassNameValue; container?: ClassNameValue; wrapper?: ClassNameValue; header?: ClassNameValue; ... 5 more ...; description?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`header`| `{}`  
`body`| `{}`  
`leading`| `{}`  
`title`| `{}`  
`description`| `{}`  
`footer`| `{}`  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageCard: {
          slots: {
            root: 'relative flex rounded-lg',
            spotlight: 'absolute inset-0 rounded-[inherit] pointer-events-none bg-default/90',
            container: 'relative flex flex-col flex-1 lg:grid gap-x-8 gap-y-4 p-4 sm:p-6',
            wrapper: 'flex flex-col flex-1',
            header: 'mb-4',
            body: 'flex-1',
            footer: 'pt-4 mt-auto',
            leading: 'inline-flex items-center mb-2.5',
            leadingIcon: 'size-5 shrink-0 text-primary',
            title: 'text-base text-pretty font-semibold text-highlighted',
            description: 'text-[15px] text-pretty'
          },
          variants: {
            orientation: {
              horizontal: {
                container: 'lg:grid-cols-2 lg:items-center'
              },
              vertical: {
                container: ''
              }
            },
            reverse: {
              true: {
                wrapper: 'lg:order-last'
              }
            },
            variant: {
              solid: {
                root: 'bg-inverted text-inverted',
                title: 'text-inverted',
                description: 'text-dimmed'
              },
              outline: {
                root: 'bg-default ring ring-default',
                description: 'text-muted'
              },
              soft: {
                root: 'bg-elevated/50',
                description: 'text-toned'
              },
              subtle: {
                root: 'bg-elevated/50 ring ring-default',
                description: 'text-toned'
              },
              ghost: {
                description: 'text-muted'
              },
              naked: {
                container: 'p-0 sm:p-0',
                description: 'text-muted'
              }
            },
            to: {
              true: {
                root: [
                  'transition'
                ]
              }
            },
            title: {
              true: {
                description: 'mt-1'
              }
            },
            highlight: {
              true: {
                root: 'ring-2'
              }
            },
            highlightColor: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            spotlight: {
              true: {
                root: '[--spotlight-size:400px] before:absolute before:-inset-px before:pointer-events-none before:rounded-[inherit] before:bg-[radial-gradient(var(--spotlight-size)_var(--spotlight-size)_at_calc(var(--spotlight-x,0px))_calc(var(--spotlight-y,0px)),var(--spotlight-color),transparent_70%)]'
              }
            },
            spotlightColor: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            }
          },
          compoundVariants: [
            {
              variant: 'solid',
              to: true,
              class: {
                root: 'hover:bg-inverted/90'
              }
            },
            {
              variant: 'outline',
              to: true,
              class: {
                root: 'hover:bg-elevated/50'
              }
            },
            {
              variant: 'soft',
              to: true,
              class: {
                root: 'hover:bg-elevated'
              }
            },
            {
              variant: 'subtle',
              to: true,
              class: {
                root: 'hover:bg-elevated'
              }
            },
            {
              variant: 'subtle',
              to: true,
              highlight: false,
              class: {
                root: 'hover:ring-accented'
              }
            },
            {
              variant: 'ghost',
              to: true,
              class: {
                root: 'hover:bg-elevated/50'
              }
            },
            {
              highlightColor: 'primary',
              highlight: true,
              class: {
                root: 'ring-primary'
              }
            },
            {
              highlightColor: 'neutral',
              highlight: true,
              class: {
                root: 'ring-inverted'
              }
            },
            {
              spotlightColor: 'primary',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-primary)]'
              }
            },
            {
              spotlightColor: 'secondary',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-secondary)]'
              }
            },
            {
              spotlightColor: 'success',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-success)]'
              }
            },
            {
              spotlightColor: 'info',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-info)]'
              }
            },
            {
              spotlightColor: 'warning',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-warning)]'
              }
            },
            {
              spotlightColor: 'error',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-error)]'
              }
            },
            {
              spotlightColor: 'neutral',
              spotlight: true,
              class: {
                root: '[--spotlight-color:var(--ui-bg-inverted)]'
              }
            }
          ],
          defaultVariants: {
            variant: 'outline',
            highlightColor: 'primary',
            spotlightColor: 'primary'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            pageCard: {
              slots: {
                root: 'relative flex rounded-lg',
                spotlight: 'absolute inset-0 rounded-[inherit] pointer-events-none bg-default/90',
                container: 'relative flex flex-col flex-1 lg:grid gap-x-8 gap-y-4 p-4 sm:p-6',
                wrapper: 'flex flex-col flex-1',
                header: 'mb-4',
                body: 'flex-1',
                footer: 'pt-4 mt-auto',
                leading: 'inline-flex items-center mb-2.5',
                leadingIcon: 'size-5 shrink-0 text-primary',
                title: 'text-base text-pretty font-semibold text-highlighted',
                description: 'text-[15px] text-pretty'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center'
                  },
                  vertical: {
                    container: ''
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'lg:order-last'
                  }
                },
                variant: {
                  solid: {
                    root: 'bg-inverted text-inverted',
                    title: 'text-inverted',
                    description: 'text-dimmed'
                  },
                  outline: {
                    root: 'bg-default ring ring-default',
                    description: 'text-muted'
                  },
                  soft: {
                    root: 'bg-elevated/50',
                    description: 'text-toned'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default',
                    description: 'text-toned'
                  },
                  ghost: {
                    description: 'text-muted'
                  },
                  naked: {
                    container: 'p-0 sm:p-0',
                    description: 'text-muted'
                  }
                },
                to: {
                  true: {
                    root: [
                      'transition'
                    ]
                  }
                },
                title: {
                  true: {
                    description: 'mt-1'
                  }
                },
                highlight: {
                  true: {
                    root: 'ring-2'
                  }
                },
                highlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                spotlight: {
                  true: {
                    root: '[--spotlight-size:400px] before:absolute before:-inset-px before:pointer-events-none before:rounded-[inherit] before:bg-[radial-gradient(var(--spotlight-size)_var(--spotlight-size)_at_calc(var(--spotlight-x,0px))_calc(var(--spotlight-y,0px)),var(--spotlight-color),transparent_70%)]'
                  }
                },
                spotlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                }
              },
              compoundVariants: [
                {
                  variant: 'solid',
                  to: true,
                  class: {
                    root: 'hover:bg-inverted/90'
                  }
                },
                {
                  variant: 'outline',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50'
                  }
                },
                {
                  variant: 'soft',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated'
                  }
                },
                {
                  variant: 'subtle',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated'
                  }
                },
                {
                  variant: 'subtle',
                  to: true,
                  highlight: false,
                  class: {
                    root: 'hover:ring-accented'
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50'
                  }
                },
                {
                  highlightColor: 'primary',
                  highlight: true,
                  class: {
                    root: 'ring-primary'
                  }
                },
                {
                  highlightColor: 'neutral',
                  highlight: true,
                  class: {
                    root: 'ring-inverted'
                  }
                },
                {
                  spotlightColor: 'primary',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-primary)]'
                  }
                },
                {
                  spotlightColor: 'secondary',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-secondary)]'
                  }
                },
                {
                  spotlightColor: 'success',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-success)]'
                  }
                },
                {
                  spotlightColor: 'info',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-info)]'
                  }
                },
                {
                  spotlightColor: 'warning',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-warning)]'
                  }
                },
                {
                  spotlightColor: 'error',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-error)]'
                  }
                },
                {
                  spotlightColor: 'neutral',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-bg-inverted)]'
                  }
                }
              ],
              defaultVariants: {
                variant: 'outline',
                highlightColor: 'primary',
                spotlightColor: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            pageCard: {
              slots: {
                root: 'relative flex rounded-lg',
                spotlight: 'absolute inset-0 rounded-[inherit] pointer-events-none bg-default/90',
                container: 'relative flex flex-col flex-1 lg:grid gap-x-8 gap-y-4 p-4 sm:p-6',
                wrapper: 'flex flex-col flex-1',
                header: 'mb-4',
                body: 'flex-1',
                footer: 'pt-4 mt-auto',
                leading: 'inline-flex items-center mb-2.5',
                leadingIcon: 'size-5 shrink-0 text-primary',
                title: 'text-base text-pretty font-semibold text-highlighted',
                description: 'text-[15px] text-pretty'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center'
                  },
                  vertical: {
                    container: ''
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'lg:order-last'
                  }
                },
                variant: {
                  solid: {
                    root: 'bg-inverted text-inverted',
                    title: 'text-inverted',
                    description: 'text-dimmed'
                  },
                  outline: {
                    root: 'bg-default ring ring-default',
                    description: 'text-muted'
                  },
                  soft: {
                    root: 'bg-elevated/50',
                    description: 'text-toned'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default',
                    description: 'text-toned'
                  },
                  ghost: {
                    description: 'text-muted'
                  },
                  naked: {
                    container: 'p-0 sm:p-0',
                    description: 'text-muted'
                  }
                },
                to: {
                  true: {
                    root: [
                      'transition'
                    ]
                  }
                },
                title: {
                  true: {
                    description: 'mt-1'
                  }
                },
                highlight: {
                  true: {
                    root: 'ring-2'
                  }
                },
                highlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                spotlight: {
                  true: {
                    root: '[--spotlight-size:400px] before:absolute before:-inset-px before:pointer-events-none before:rounded-[inherit] before:bg-[radial-gradient(var(--spotlight-size)_var(--spotlight-size)_at_calc(var(--spotlight-x,0px))_calc(var(--spotlight-y,0px)),var(--spotlight-color),transparent_70%)]'
                  }
                },
                spotlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                }
              },
              compoundVariants: [
                {
                  variant: 'solid',
                  to: true,
                  class: {
                    root: 'hover:bg-inverted/90'
                  }
                },
                {
                  variant: 'outline',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50'
                  }
                },
                {
                  variant: 'soft',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated'
                  }
                },
                {
                  variant: 'subtle',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated'
                  }
                },
                {
                  variant: 'subtle',
                  to: true,
                  highlight: false,
                  class: {
                    root: 'hover:ring-accented'
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50'
                  }
                },
                {
                  highlightColor: 'primary',
                  highlight: true,
                  class: {
                    root: 'ring-primary'
                  }
                },
                {
                  highlightColor: 'neutral',
                  highlight: true,
                  class: {
                    root: 'ring-inverted'
                  }
                },
                {
                  spotlightColor: 'primary',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-primary)]'
                  }
                },
                {
                  spotlightColor: 'secondary',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-secondary)]'
                  }
                },
                {
                  spotlightColor: 'success',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-success)]'
                  }
                },
                {
                  spotlightColor: 'info',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-info)]'
                  }
                },
                {
                  spotlightColor: 'warning',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-warning)]'
                  }
                },
                {
                  spotlightColor: 'error',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-error)]'
                  }
                },
                {
                  spotlightColor: 'neutral',
                  spotlight: true,
                  class: {
                    root: '[--spotlight-color:var(--ui-bg-inverted)]'
                  }
                }
              ],
              defaultVariants: {
                variant: 'outline',
                highlightColor: 'primary',
                spotlightColor: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui-pro/blob/v3/src/theme/page-card.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[PageBodyThe main content of your page.](/components/page-body)[PageColumnsA
responsive multi-column layout system for organizing content side-by-
side.](/components/page-columns)

