<!-- source: https://ui.nuxt.com/components/page-hero --> # PageHeroPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageHero.vue)

A responsive hero for your pages.

## Usage

The PageHero component wraps your content in a
[Container](/components/container) while maintaining full-width flexibility
making it easy to add background colors, images or patterns. It provides a
flexible way to display content with an illustration in the default slot.

# Ultimate Vue UI library

A Nuxt/Vue-integrated UI library providing a rich set of fully-styled,
accessible and highly customizable components for building modern web
applications.

![App screenshot](https://ui.nuxt.com/templates/dashboard1.png)

### Title

Use the `title` prop to set the title of the hero.

title

# Ultimate Vue UI library

    
    
    <template>
      <UPageHero title="Ultimate Vue UI library" />
    </template>
    

### Description

Use the `description` prop to set the description of the hero.

description

# Ultimate Vue UI library

A Nuxt/Vue-integrated UI library providing a rich set of fully-styled,
accessible and highly customizable components for building modern web
applications.

    
    
    <template>
      <UPageHero
        title="Ultimate Vue UI library"
        description="A Nuxt/Vue-integrated UI library providing a rich set of fully-styled, accessible and highly customizable components for building modern web applications."
      />
    </template>
    

### Headline

Use the `headline` prop to set the headline of the hero.

headline

New release

# Ultimate Vue UI library

A Nuxt/Vue-integrated UI library providing a rich set of fully-styled,
accessible and highly customizable components for building modern web
applications.

    
    
    <template>
      <UPageHero
        title="Ultimate Vue UI library"
        description="A Nuxt/Vue-integrated UI library providing a rich set of fully-styled, accessible and highly customizable components for building modern web applications."
        headline="New release"
      />
    </template>
    

### Links

Use the `links` prop to display a list of [Button](/components/button) under
the description.

# Ultimate Vue UI library

A Nuxt/Vue-integrated UI library providing a rich set of fully-styled,
accessible and highly customizable components for building modern web
applications.

[Get started](/getting-started)[Learn more](/getting-started/theme)

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        to: '/getting-started',
        icon: 'i-lucide-square-play'
      },
      {
        label: 'Learn more',
        to: '/getting-started/theme',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageHero
        title="Ultimate Vue UI library"
        description="A Nuxt/Vue-integrated UI library providing a rich set of fully-styled, accessible and highly customizable components for building modern web applications."
        :links="links"
      />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation with the default slot.
Defaults to `vertical`.

orientation

horizontal

New release

# Ultimate Vue UI library

A Nuxt/Vue-integrated UI library providing a rich set of fully-styled,
accessible and highly customizable components for building modern web
applications.

[Get started](/getting-started)[Learn more](/getting-started/theme)

![App screenshot](https://ui.nuxt.com/templates/dashboard1.png)

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        to: '/getting-started',
        icon: 'i-lucide-square-play'
      },
      {
        label: 'Learn more',
        to: '/getting-started/theme',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageHero
        title="Ultimate Vue UI library"
        description="A Nuxt/Vue-integrated UI library providing a rich set of fully-styled, accessible and highly customizable components for building modern web applications."
        headline="New release"
        orientation="horizontal"
        :links="links"
      >
        <img
          src="https://ui.nuxt.com/templates/dashboard1.png"
          alt="App screenshot"
          class="rounded-lg shadow-2xl ring ring-default"
        />
      </UPageHero>
    </template>
    

### Reverse

Use the `reverse` prop to reverse the orientation of the default slot.

orientation

horizontal

reverse

true

New release

# Ultimate Vue UI library

A Nuxt/Vue-integrated UI library providing a rich set of fully-styled,
accessible and highly customizable components for building modern web
applications.

[Get started](/getting-started)[Learn more](/getting-started/theme)

![App screenshot](https://ui.nuxt.com/templates/dashboard1.png)

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        to: '/getting-started',
        icon: 'i-lucide-square-play'
      },
      {
        label: 'Learn more',
        to: '/getting-started/theme',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageHero
        title="Ultimate Vue UI library"
        description="A Nuxt/Vue-integrated UI library providing a rich set of fully-styled, accessible and highly customizable components for building modern web applications."
        headline="New release"
        orientation="horizontal"
        reverse
        :links="links"
      >
        <img
          src="https://ui.nuxt.com/templates/dashboard1.png"
          alt="App screenshot"
          class="rounded-lg shadow-2xl ring ring-default"
        />
      </UPageHero>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`  
`reverse`| `false`| `boolean`Reverse the order of the default slot.  
`title`| | ` string`  
`description`| | ` string`  
`links`| | ` ButtonProps[]`Display a list of Button under the description. `{ size: 'xl' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`headline`| | ` string`  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; wrapper?: ClassNameValue; headline?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; links?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`top`| `{}`  
`bottom`| `{}`  
`headline`| `{}`  
`title`| `{}`  
`description`| `{}`  
`links`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageHero: {
          slots: {
            root: 'relative isolate',
            container: 'flex flex-col lg:grid py-24 sm:py-32 lg:py-40 gap-16 sm:gap-y-24',
            wrapper: '',
            headline: 'mb-4',
            title: 'text-5xl sm:text-7xl text-pretty tracking-tight font-bold text-highlighted',
            description: 'text-lg sm:text-xl/8 text-muted',
            links: 'mt-10 flex flex-wrap gap-x-6 gap-y-3'
          },
          variants: {
            orientation: {
              horizontal: {
                container: 'lg:grid-cols-2 lg:items-center',
                description: 'text-pretty'
              },
              vertical: {
                container: '',
                headline: 'justify-center',
                wrapper: 'text-center',
                description: 'text-balance',
                links: 'justify-center'
              }
            },
            reverse: {
              true: {
                wrapper: 'order-last'
              }
            },
            headline: {
              true: {
                headline: 'font-semibold text-primary flex items-center gap-1.5'
              }
            },
            title: {
              true: {
                description: 'mt-6'
              }
            }
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
            pageHero: {
              slots: {
                root: 'relative isolate',
                container: 'flex flex-col lg:grid py-24 sm:py-32 lg:py-40 gap-16 sm:gap-y-24',
                wrapper: '',
                headline: 'mb-4',
                title: 'text-5xl sm:text-7xl text-pretty tracking-tight font-bold text-highlighted',
                description: 'text-lg sm:text-xl/8 text-muted',
                links: 'mt-10 flex flex-wrap gap-x-6 gap-y-3'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center',
                    description: 'text-pretty'
                  },
                  vertical: {
                    container: '',
                    headline: 'justify-center',
                    wrapper: 'text-center',
                    description: 'text-balance',
                    links: 'justify-center'
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'order-last'
                  }
                },
                headline: {
                  true: {
                    headline: 'font-semibold text-primary flex items-center gap-1.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-6'
                  }
                }
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
            pageHero: {
              slots: {
                root: 'relative isolate',
                container: 'flex flex-col lg:grid py-24 sm:py-32 lg:py-40 gap-16 sm:gap-y-24',
                wrapper: '',
                headline: 'mb-4',
                title: 'text-5xl sm:text-7xl text-pretty tracking-tight font-bold text-highlighted',
                description: 'text-lg sm:text-xl/8 text-muted',
                links: 'mt-10 flex flex-wrap gap-x-6 gap-y-3'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center',
                    description: 'text-pretty'
                  },
                  vertical: {
                    container: '',
                    headline: 'justify-center',
                    wrapper: 'text-center',
                    description: 'text-balance',
                    links: 'justify-center'
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'order-last'
                  }
                },
                headline: {
                  true: {
                    headline: 'font-semibold text-primary flex items-center gap-1.5'
                  }
                },
                title: {
                  true: {
                    description: 'mt-6'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageHeaderA responsive header for your pages.](/components/page-
header)[PageLinksA list of links to be displayed in the
page.](/components/page-links)

